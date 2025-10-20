"""
Board class for Djambi game.
Manages the 9x9 game board and piece positions.
"""
from typing import Optional, Tuple, List
from pieces import Piece, Team, Militant, Leader, Assassin, Necromobile, Reporter, Provocateur


class Board:
    """Manages the Djambi game board and piece positions."""

    def __init__(self):
        """Initialize a 9x9 board with starting positions."""
        # Use 11x11 grid for easier indexing (0 and 10 are borders, 1-9 are playable)
        self.grid: List[List[Optional[Piece]]] = [[None for _ in range(11)] for _ in range(11)]
        self._setup_initial_positions()

    def _setup_initial_positions(self):
        """Set up the initial piece positions for all 4 teams."""
        # Team 1 (Red) - Top-left corner
        self.grid[1][1] = Leader(Team.RED)
        self.grid[1][2] = Assassin(Team.RED)
        self.grid[1][3] = Militant(Team.RED)
        self.grid[2][1] = Reporter(Team.RED)
        self.grid[2][2] = Provocateur(Team.RED)
        self.grid[2][3] = Militant(Team.RED)
        self.grid[3][1] = Militant(Team.RED)
        self.grid[3][2] = Militant(Team.RED)
        self.grid[3][3] = Necromobile(Team.RED)

        # Team 2 (Blue) - Top-right corner
        self.grid[1][7] = Militant(Team.BLUE)
        self.grid[1][8] = Assassin(Team.BLUE)
        self.grid[1][9] = Leader(Team.BLUE)
        self.grid[2][7] = Militant(Team.BLUE)
        self.grid[2][8] = Provocateur(Team.BLUE)
        self.grid[2][9] = Reporter(Team.BLUE)
        self.grid[3][7] = Necromobile(Team.BLUE)
        self.grid[3][8] = Militant(Team.BLUE)
        self.grid[3][9] = Militant(Team.BLUE)

        # Team 3 (Yellow) - Bottom-left corner
        self.grid[7][1] = Militant(Team.YELLOW)
        self.grid[7][2] = Militant(Team.YELLOW)
        self.grid[7][3] = Necromobile(Team.YELLOW)
        self.grid[8][1] = Reporter(Team.YELLOW)
        self.grid[8][2] = Provocateur(Team.YELLOW)
        self.grid[8][3] = Militant(Team.YELLOW)
        self.grid[9][1] = Leader(Team.YELLOW)
        self.grid[9][2] = Assassin(Team.YELLOW)
        self.grid[9][3] = Militant(Team.YELLOW)

        # Team 4 (Green) - Bottom-right corner
        self.grid[7][7] = Necromobile(Team.GREEN)
        self.grid[7][8] = Militant(Team.GREEN)
        self.grid[7][9] = Militant(Team.GREEN)
        self.grid[8][7] = Militant(Team.GREEN)
        self.grid[8][8] = Provocateur(Team.GREEN)
        self.grid[8][9] = Reporter(Team.GREEN)
        self.grid[9][7] = Militant(Team.GREEN)
        self.grid[9][8] = Assassin(Team.GREEN)
        self.grid[9][9] = Leader(Team.GREEN)

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        """
        Get the piece at the given position.

        Args:
            row: Row position (1-9)
            col: Column position (1-9)

        Returns:
            The piece at that position, or None if empty
        """
        if not (1 <= row <= 9 and 1 <= col <= 9):
            return None
        return self.grid[row][col]

    def set_piece(self, row: int, col: int, piece: Optional[Piece]):
        """
        Set a piece at the given position.

        Args:
            row: Row position (1-9)
            col: Column position (1-9)
            piece: The piece to place, or None to clear the square
        """
        if 1 <= row <= 9 and 1 <= col <= 9:
            self.grid[row][col] = piece

    def find_piece_position(self, piece: Piece) -> Optional[Tuple[int, int]]:
        """
        Find the position of a specific piece on the board.

        Args:
            piece: The piece to find

        Returns:
            (row, col) tuple if found, None otherwise
        """
        for row in range(1, 10):
            for col in range(1, 10):
                if self.grid[row][col] is piece:
                    return (row, col)
        return None

    def is_path_clear(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        """
        Check if the path between two positions is clear (no pieces in between).

        Args:
            from_row: Starting row
            from_col: Starting column
            to_row: Ending row
            to_col: Ending column

        Returns:
            True if path is clear, False otherwise
        """
        # Calculate direction
        row_diff = to_row - from_row
        col_diff = to_col - from_col

        # Not a valid straight/diagonal line
        if row_diff != 0 and col_diff != 0 and abs(row_diff) != abs(col_diff):
            return False

        # Normalize to -1, 0, or 1
        row_step = 0 if row_diff == 0 else (1 if row_diff > 0 else -1)
        col_step = 0 if col_diff == 0 else (1 if col_diff > 0 else -1)

        # Check each square along the path (excluding start and end)
        current_row = from_row + row_step
        current_col = from_col + col_step

        while (current_row, current_col) != (to_row, to_col):
            if self.grid[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step

        return True

    def is_valid_move(self, piece: Piece, from_row: int, from_col: int,
                      to_row: int, to_col: int) -> bool:
        """
        Check if a move is valid for the given piece.

        Args:
            piece: The piece to move
            from_row: Starting row
            from_col: Starting column
            to_row: Ending row
            to_col: Ending column

        Returns:
            True if move is valid, False otherwise
        """
        # Check bounds
        if not (1 <= to_row <= 9 and 1 <= to_col <= 9):
            return False

        # Check if move is in the piece's possible moves
        possible_moves = piece.get_possible_moves(self, from_row, from_col)
        return (to_row, to_col) in possible_moves

    def move_piece(self, from_row: int, from_col: int, to_row: int, to_col: int) -> Optional[Piece]:
        """
        Move a piece from one position to another.

        Args:
            from_row: Starting row
            from_col: Starting column
            to_row: Ending row
            to_col: Ending column

        Returns:
            The captured piece (if any), or None
        """
        piece = self.grid[from_row][from_col]
        captured = self.grid[to_row][to_col]

        # Move the piece
        self.grid[to_row][to_col] = piece
        self.grid[from_row][from_col] = None

        # If a piece was captured, mark it as dead
        if captured:
            captured.kill()

        return captured

    def get_team_pieces(self, team: Team) -> List[Tuple[Piece, int, int]]:
        """
        Get all pieces for a given team.

        Args:
            team: The team to get pieces for

        Returns:
            List of (piece, row, col) tuples
        """
        pieces = []
        for row in range(1, 10):
            for col in range(1, 10):
                piece = self.grid[row][col]
                if piece and piece.team == team:
                    pieces.append((piece, row, col))
        return pieces

    def has_valid_moves(self, team: Team) -> bool:
        """
        Check if a team has any valid moves available.

        Args:
            team: The team to check

        Returns:
            True if team has valid moves, False otherwise
        """
        for piece, row, col in self.get_team_pieces(team):
            if not piece.is_alive:
                continue
            if piece.get_possible_moves(self, row, col):
                return True
        return False

    def is_leader_trapped(self, team: Team) -> bool:
        """
        Check if a team's leader is trapped by dead pieces with no necromobile.

        Args:
            team: The team to check

        Returns:
            True if leader is trapped, False otherwise
        """
        # Find the leader
        leader = None
        leader_pos = None
        necromobile = None

        for piece, row, col in self.get_team_pieces(team):
            if piece.piece_type.name == "LEADER" and piece.is_alive:
                leader = piece
                leader_pos = (row, col)
            if piece.piece_type.name == "NECROMOBILE" and piece.is_alive:
                necromobile = piece

        # If no leader or leader is dead, not trapped
        if not leader or not leader.is_alive:
            return False

        # If necromobile is alive, can potentially clear dead pieces
        if necromobile:
            return False

        # Check if all 8 surrounding squares are blocked by dead pieces or borders
        row, col = leader_pos
        surrounding = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1),                 (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]

        for r, c in surrounding:
            # Out of bounds
            if not (1 <= r <= 9 and 1 <= c <= 9):
                continue
            # Empty square or live piece (could potentially move)
            piece = self.grid[r][c]
            if piece is None or piece.is_alive:
                return False

        return True

    def __str__(self) -> str:
        """Return a string representation of the board."""
        lines = []
        lines.append("  1 2 3 4 5 6 7 8 9")
        for row in range(1, 10):
            line = f"{row} "
            for col in range(1, 10):
                piece = self.grid[row][col]
                if piece:
                    line += piece.get_display_char() + " "
                else:
                    line += ". "
            lines.append(line)
        return "\n".join(lines)
