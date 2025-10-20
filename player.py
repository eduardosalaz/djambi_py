"""
Player class for Djambi game.
"""
from pieces import Team, Piece, PieceType


class Player:
    """Represents a player/team in the game."""

    def __init__(self, team: Team):
        self.team = team
        self.is_eliminated = False

    def __repr__(self):
        status = "eliminated" if self.is_eliminated else "active"
        return f"Player({self.team.name}, {status})"

    def eliminate(self):
        """Mark this player as eliminated."""
        self.is_eliminated = True

    def get_team_name(self) -> str:
        """Get the localized team name (Spanish)."""
        names = {
            Team.RED: "Rojo",
            Team.BLUE: "Azul",
            Team.YELLOW: "Amarillo",
            Team.GREEN: "Verde"
        }
        return names[self.team]

    def check_elimination(self, board: 'Board') -> bool:
        """
        Check if this player should be eliminated (leader is dead).

        Args:
            board: The game board

        Returns:
            True if player should be eliminated, False otherwise
        """
        # Find the leader
        for piece, row, col in board.get_team_pieces(self.team):
            if piece.piece_type == PieceType.LEADER:
                if not piece.is_alive:
                    self.eliminate()
                    return True
        return False
