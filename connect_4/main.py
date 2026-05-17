from dataclasses import dataclass
from enum import Enum

import pygame

ROWS = 6
COLUMNS = 7
PIECE_SIZE = 100
BORDER_SIZE = 1
width = PIECE_SIZE * COLUMNS
height = PIECE_SIZE * (ROWS + 2) # some space

class Piece(Enum):
    EMPTY = 0
    RED = 1
    BLUE = 2

class State(Enum):
    PLAYED = 0
    INVALID_MOVE = 1
    WON = 2

@dataclass(frozen=True)
class Move():
    state: State
    error_msg: str = ""

class Board:
    def __init__(self):
        self.board = [[Piece.EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.winner = None
        self.moves = [
            pygame.math.Vector2(0, 1),
            pygame.math.Vector2(1, 0),
            pygame.math.Vector2(1, 1),
            pygame.math.Vector2(-1, 1),
        ]
        self.past_moves = []
        self.playing = Piece.BLUE
        self.finished = False
    
    def _get_first(self, piece: Piece, pos: pygame.math.Vector2, mov: pygame.math.Vector2) -> pygame.math.Vector2:
        while pos[0] >= 0 and pos[0] < len(self.board)\
                and pos[1] >= 0 and pos[1] < len(self.board[0])\
                and piece == self.board[int(pos[0])][int(pos[1])]:
            pos = pos + mov
        return pos - mov
    
    def _is_win(self, piece: Piece, pos: pygame.math.Vector2, mov: pygame.math.Vector2) -> bool:
        first = self._get_first(piece, pos, mov)
        last = self._get_first(piece, pos, -mov)
        diff = last - first
        if abs(diff[0]) == 3 or abs(diff[1]) == 3:
            return True
        return False

    def play(self, col: int) -> Move:
        if col < 0 or col >= COLUMNS: raise RuntimeError(f"Unexpected value for column: {col}")
        if self.finished:
            return Move(state=State.INVALID_MOVE, error_msg=f"Player {self.playing} already won")

        piece = self.playing
        empty_place = -1
        for i in range(len(self.board)):
            if Piece.EMPTY == self.board[i][col]:
                empty_place = i
                self.board[i][col] = piece
                break
        
        if empty_place == -1: return Move(state=State.INVALID_MOVE, error_msg=f"The column {col} is full, cannot add piece")

        # check win condition
        pos = pygame.math.Vector2(empty_place, col)
        self.past_moves.append(pos)

        if any([self._is_win(piece, pos, mov) for mov in self.moves]):
            self.finished = True
            return Move(state=State.WON)
        self.playing = Piece.BLUE if self.playing == Piece.RED else Piece.RED
        return Move(state=State.PLAYED)
    
    def undo(self):
        if not self.past_moves:
            return
        last = self.past_moves.pop()
        self.playing = self.board[int(last[0])][int(last[1])]
        self.board[int(last[0])][int(last[1])] = Piece.EMPTY
        self.finished = False

def int_to_key(n):
    return getattr(pygame, f'K_{n}')

def key_to_col(key):
    for n in range(1, COLUMNS + 1):
        if key == int_to_key(n):
            return n - 1
    return -1

def main():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Connect 4')

    number_font = pygame.font.Font(None, 30)
    text_font = pygame.font.Font(None, 60)

    board = Board()

    def reset():
        nonlocal board
        board = Board()

    while True:
        col = -1
        doReset = False
        undo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                col = key_to_col(event.key)
                if event.key == pygame.K_r:
                    doReset = True
                if event.key == pygame.K_BACKSPACE:
                    undo = True
        if doReset:
            reset()
        elif col != -1:
            playing = board.playing
            move = board.play(col)
            if move.state == State.WON:
                print(f"Player {playing} won")
            elif move.state == State.INVALID_MOVE:
                print(f"Invalid move: {move.error_msg}")
        elif undo:
            board.undo()

        screen.fill('#000000')
        for r, row in enumerate(board.board):
            for c, piece in enumerate(row):
                color = "#C2C294"
                pygame.draw.rect(screen, color, (c * PIECE_SIZE, (len(board.board) - r) * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))
        for r, row in enumerate(board.board):
            for c, piece in enumerate(row):
                color = "#002FFF" if piece == Piece.BLUE else "#FF002B" if piece == Piece.RED else "#ffffff"
                pygame.draw.rect(screen, color, (c * PIECE_SIZE, (len(board.board) - r) * PIECE_SIZE, PIECE_SIZE - BORDER_SIZE, PIECE_SIZE - BORDER_SIZE))
        for c, col in enumerate(board.board[0]):
            number_surface = number_font.render(f"{c + 1}", False, "#DBF694")
            number_rec = number_surface.get_rect(midbottom=(int((c + 0.5) * PIECE_SIZE), PIECE_SIZE))
            screen.blit(number_surface, number_rec)
        if board.finished:
            won_surface = text_font.render(f"{'BLUE' if board.playing == Piece.BLUE else 'RED'} WON", False, "#7CE18B")
            won_rect = won_surface.get_rect(midbottom=(int(width * 0.5), int(height * 0.5)))
            screen.blit(won_surface, won_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()