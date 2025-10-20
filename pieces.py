"""
Piece classes for Djambi game.
Refactored from arithmetic encoding to clean OOP design.
"""
from enum import Enum
from typing import List, Tuple, Optional


class PieceType(Enum):
    """Enum for piece types."""
    MILITANT = "M"      # Militante
    NECROMOBILE = "N"   # Necromóvil
    REPORTER = "R"      # Reportero
    PROVOCATEUR = "P"   # Provocador
    LEADER = "L"        # Líder
    ASSASSIN = "A"      # Asesino


class Team(Enum):
    """Enum for team colors."""
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4


class Piece:
    """Base class for all Djambi pieces."""

    def __init__(self, team: Team, piece_type: PieceType):
        self.team = team
        self.piece_type = piece_type
        self.is_alive = True

    def __repr__(self):
        status = "alive" if self.is_alive else "dead"
        return f"{self.piece_type.name}({self.team.name}, {status})"

    def get_display_char(self) -> str:
        """Return the character to display on the board."""
        return self.piece_type.value

    def kill(self):
        """Mark this piece as captured/dead."""
        self.is_alive = False

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """
        Get all possible moves for this piece from the given position.
        Must be implemented by subclasses.

        Args:
            board: The game board
            row: Current row position (1-9)
            col: Current column position (1-9)

        Returns:
            List of (row, col) tuples representing valid moves
        """
        raise NotImplementedError("Subclasses must implement get_possible_moves")

    def can_capture(self, target: Optional['Piece']) -> bool:
        """
        Check if this piece can capture the target piece.
        Can be overridden by subclasses with special capture rules.

        Args:
            target: The piece to potentially capture (or None for empty square)

        Returns:
            True if capture is allowed, False otherwise
        """
        if target is None:
            return False
        if target.team == self.team:
            return False
        if not target.is_alive:
            return False
        return True


class Militant(Piece):
    """
    Militante - Can move max 2 squares in any direction.
    Cannot capture the leader in the center square.
    """

    def __init__(self, team: Team):
        super().__init__(team, PieceType.MILITANT)
        self.max_distance = 2

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """Get all valid moves for a Militant (max 2 squares in any direction)."""
        moves = []

        # Check all 8 directions, up to 2 squares away
        for dr in [-2, -1, 0, 1, 2]:
            for dc in [-2, -1, 0, 1, 2]:
                if dr == 0 and dc == 0:
                    continue

                new_row = row + dr
                new_col = col + dc

                # Check bounds
                if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                    continue

                # Check path is clear (can't jump pieces)
                if not board.is_path_clear(row, col, new_row, new_col):
                    continue

                target = board.get_piece(new_row, new_col)

                # Can move to empty square
                if target is None:
                    moves.append((new_row, new_col))
                # Can capture enemy pieces (except leader in center)
                elif self.can_capture(target):
                    if not (new_row == 5 and new_col == 5 and target.piece_type == PieceType.LEADER):
                        moves.append((new_row, new_col))

        return moves

    def can_capture(self, target: Optional[Piece]) -> bool:
        """Militants can't capture dead pieces or leaders in center."""
        if not super().can_capture(target):
            return False
        return True


class Leader(Piece):
    """
    Líder - Can move max 8 squares in any direction.
    Only piece that can occupy the center square (5, 5).
    Most important piece - losing it means elimination.
    """

    def __init__(self, team: Team):
        super().__init__(team, PieceType.LEADER)
        self.max_distance = 8

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """Get all valid moves for a Leader (max 8 squares in straight/diagonal lines)."""
        moves = []

        # 8 directions: N, NE, E, SE, S, SW, W, NW
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for dr, dc in directions:
            for distance in range(1, 9):
                new_row = row + dr * distance
                new_col = col + dc * distance

                # Check bounds
                if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                    break

                target = board.get_piece(new_row, new_col)

                # Empty square - can move here
                if target is None:
                    moves.append((new_row, new_col))
                # Blocked by piece
                else:
                    # Can capture enemy piece
                    if self.can_capture(target):
                        moves.append((new_row, new_col))
                    # Can't jump over pieces
                    break

        return moves


class Assassin(Piece):
    """
    Asesino - Can move max 8 squares in any direction.
    When capturing, swaps position with captured piece (assassin's special ability).
    """

    def __init__(self, team: Team):
        super().__init__(team, PieceType.ASSASSIN)
        self.max_distance = 8

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """Get all valid moves for an Assassin (max 8 squares, swaps on capture)."""
        moves = []

        # 8 directions
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for dr, dc in directions:
            for distance in range(1, 9):
                new_row = row + dr * distance
                new_col = col + dc * distance

                # Check bounds
                if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                    break

                target = board.get_piece(new_row, new_col)

                # Empty square - can move here
                if target is None:
                    moves.append((new_row, new_col))
                # Blocked by piece
                else:
                    # Can capture enemy piece
                    if self.can_capture(target):
                        moves.append((new_row, new_col))
                    # Can't jump over pieces
                    break

        return moves


class Necromobile(Piece):
    """
    Necromóvil - Can move max 8 squares in any direction.
    Cannot capture live pieces, but can move dead (captured) pieces to empty squares.
    Cannot place pieces in the center square.
    """

    def __init__(self, team: Team):
        super().__init__(team, PieceType.NECROMOBILE)
        self.max_distance = 8

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """Get all valid moves for a Necromobile (can only move to empty or dead pieces)."""
        moves = []

        # 8 directions
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for dr, dc in directions:
            for distance in range(1, 9):
                new_row = row + dr * distance
                new_col = col + dc * distance

                # Check bounds
                if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                    break

                target = board.get_piece(new_row, new_col)

                # Empty square - can move here
                if target is None:
                    moves.append((new_row, new_col))
                # Can move to dead enemy piece
                elif not target.is_alive and target.team != self.team:
                    moves.append((new_row, new_col))
                # Blocked by any living piece
                else:
                    break

        return moves

    def can_capture(self, target: Optional[Piece]) -> bool:
        """Necromobile can only 'capture' (move to) dead pieces."""
        if target is None:
            return False
        if target.team == self.team:
            return False
        # Can only interact with dead pieces
        return not target.is_alive


class Reporter(Piece):
    """
    Reportero - Can move max 8 squares in any direction.
    Can only capture adjacent pieces (horizontally or vertically, not diagonally).
    Captured piece stays in place (doesn't move).
    """

    def __init__(self, team: Team):
        super().__init__(team, PieceType.REPORTER)
        self.max_distance = 8

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """
        Get all valid moves for a Reporter.
        Can move anywhere in straight/diagonal lines, but can only capture if:
        - Adjacent (1 square away)
        - Horizontal or vertical only (not diagonal)
        """
        moves = []

        # 8 directions
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for dr, dc in directions:
            for distance in range(1, 9):
                new_row = row + dr * distance
                new_col = col + dc * distance

                # Check bounds
                if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                    break

                target = board.get_piece(new_row, new_col)

                # Empty square - can always move here
                if target is None:
                    moves.append((new_row, new_col))
                # Can't move onto pieces (captures adjacent only, not by moving onto)
                else:
                    break

        return moves

    def get_capture_targets(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """
        Get pieces that can be captured from current position.
        Reporter captures adjacent pieces horizontally/vertically only.
        """
        captures = []

        # Only orthogonal adjacent squares (not diagonal)
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        for new_row, new_col in adjacent:
            # Check bounds
            if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                continue

            target = board.get_piece(new_row, new_col)

            # Can capture adjacent enemy pieces
            if target and self.can_capture(target):
                captures.append((new_row, new_col))

        return captures


class Provocateur(Piece):
    """
    Provocador - Can move max 8 squares in any direction.
    Cannot capture pieces, but can move live enemy pieces to any empty square (except center).
    """

    def __init__(self, team: Team):
        super().__init__(team, PieceType.PROVOCATEUR)
        self.max_distance = 8

    def get_possible_moves(self, board: 'Board', row: int, col: int) -> List[Tuple[int, int]]:
        """Get all valid moves for a Provocateur (can move to empty or live enemy pieces)."""
        moves = []

        # 8 directions
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for dr, dc in directions:
            for distance in range(1, 9):
                new_row = row + dr * distance
                new_col = col + dc * distance

                # Check bounds
                if not (1 <= new_row <= 9 and 1 <= new_col <= 9):
                    break

                target = board.get_piece(new_row, new_col)

                # Empty square - can move here
                if target is None:
                    moves.append((new_row, new_col))
                # Can move to live enemy piece
                elif target.team != self.team and target.is_alive:
                    moves.append((new_row, new_col))
                # Blocked by any other piece
                else:
                    break

        return moves

    def can_capture(self, target: Optional[Piece]) -> bool:
        """Provocateur can only 'capture' (move to) live enemy pieces."""
        if target is None:
            return False
        if target.team == self.team:
            return False
        # Can only interact with live pieces
        return target.is_alive
