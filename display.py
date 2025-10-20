"""
Display module for Djambi game.
Handles all terminal rendering with ANSI colors.
"""
import os
from typing import Optional
from pieces import Team, Piece, PieceType
from board import Board


class Display:
    """Handles terminal display and rendering."""

    # ANSI color codes
    COLORS = {
        Team.RED: '\033[1;31;40m',
        Team.BLUE: '\033[1;34;40m',
        Team.YELLOW: '\033[1;33;40m',
        Team.GREEN: '\033[1;32;40m',
    }
    DEAD_COLOR = '\033[1;35;40m'
    RESET_COLOR = '\033[1;37;40m'
    HIGHLIGHT_COLOR = '\033[1;36;40m'

    @staticmethod
    def clear():
        """Clear the terminal screen."""
        os.system('clear' if os.name != 'nt' else 'cls')

    @staticmethod
    def print_title():
        """Print the game title."""
        print(r"""
____   _                 _     _
|  _ \(_) __ _ _ __ ___ | |__ (_)
| | | | |/ _` | '_ ` _ \| '_ \| |
| |_| | | (_| | | | | | | |_) | |
|____// |\__,_|_| |_| |_|_.__/|_|
    |__/

""")

    @staticmethod
    def print_instructions():
        """Print game instructions."""
        Display.print_title()
        print("Bienvenido a Djambi.\n")
        print("Objetivo:")
        print("Capturar a los demás líderes enemigos con el uso de las diferentes piezas.\n")
        print("Movimientos:")
        print("Cada jugador moverá una de sus piezas en su turno, con la posibilidad de capturar en este movimiento a una ficha contraria.")
        print("Ninguna ficha puede desplazarse a través de una casilla ocupada por otra ficha (viva o capturada).\n")
        print("Capturas:")
        print("Para capturar una pieza enemiga, el usuario debe mover una de sus piezas con capacidad de captura a una casilla en la cual pueda capturar una pieza enemiga.")
        print("Cada pieza captura de manera distinta.\n")
        input("\nPresione la tecla intro para continuar...")

    @staticmethod
    def print_piece_guide():
        """Print piece movement guide."""
        Display.clear()
        Display.print_title()

        print("L = Líder. M = Militante. A = Asesino. R = Reportero. P = Provocador. N = Necromóvil.\n")

        print("MILITANTE (M):")
        print("- Puede moverse máximo 2 casillas en cualquier dirección")
        print("- No puede capturar al líder en el centro\n")

        print("LÍDER (L):")
        print("- Puede moverse máximo 8 casillas en cualquier dirección")
        print("- Única pieza que puede ocupar la casilla central (5,5)")
        print("- Pieza más importante: si es capturado, el equipo es eliminado\n")

        print("ASESINO (A):")
        print("- Puede moverse máximo 8 casillas en cualquier dirección")
        print("- Al capturar, intercambia posición con la pieza capturada\n")

        print("NECROMÓVIL (N):")
        print("- Puede moverse máximo 8 casillas en cualquier dirección")
        print("- No puede capturar piezas vivas")
        print("- Puede mover piezas capturadas a casillas vacías (excepto el centro)\n")

        print("REPORTERO (R):")
        print("- Puede moverse máximo 8 casillas en cualquier dirección")
        print("- Solo puede capturar piezas adyacentes (horizontal/vertical, no diagonal)")
        print("- La pieza capturada no se mueve de lugar\n")

        print("PROVOCADOR (P):")
        print("- Puede moverse máximo 8 casillas en cualquier dirección")
        print("- No puede capturar piezas")
        print("- Puede mover piezas enemigas vivas a cualquier casilla vacía (excepto el centro)\n")

        input("\nPresione la tecla intro para continuar...")

    @staticmethod
    def render_board(board: Board, current_team: Optional[Team] = None,
                     highlight_positions: Optional[list] = None):
        """
        Render the game board with colors.

        Args:
            board: The game board to render
            current_team: The current team (for highlighting)
            highlight_positions: List of (row, col) positions to highlight
        """
        Display.clear()
        print(Display.RESET_COLOR + "L = Líder. M = Militante. A = Asesino. R = Reportero. P = Provocador. N = Necromóvil.")
        print("Solo se pueden ingresar números enteros del 1 al 9.\n")

        highlight_set = set(highlight_positions) if highlight_positions else set()

        # Print column numbers
        print("  ", end="")
        for col in range(1, 10):
            print(f"{col} ", end="")
        print()

        # Print board
        for row in range(1, 10):
            print(f"{row} ", end="")
            for col in range(1, 10):
                piece = board.get_piece(row, col)

                # Center square
                if row == 5 and col == 5 and piece is None:
                    print(Display.HIGHLIGHT_COLOR + "* " + Display.RESET_COLOR, end="")
                # Highlighted position
                elif (row, col) in highlight_set:
                    if piece:
                        color = Display.COLORS[piece.team] if piece.is_alive else Display.DEAD_COLOR
                        print(color + piece.get_display_char() + " " + Display.RESET_COLOR, end="")
                    else:
                        print(Display.HIGHLIGHT_COLOR + "○ " + Display.RESET_COLOR, end="")
                # Piece
                elif piece:
                    color = Display.COLORS[piece.team] if piece.is_alive else Display.DEAD_COLOR
                    print(color + piece.get_display_char() + " " + Display.RESET_COLOR, end="")
                # Empty square
                else:
                    print(Display.RESET_COLOR + "  ", end="")

            print()

        # Print current team
        if current_team:
            color = Display.COLORS[current_team]
            team_names = {
                Team.RED: "Rojo",
                Team.BLUE: "Azul",
                Team.YELLOW: "Amarillo",
                Team.GREEN: "Verde"
            }
            print(f"\n{color}Turno del equipo {team_names[current_team]}{Display.RESET_COLOR}")

    @staticmethod
    def print_message(message: str, color: Optional[str] = None):
        """
        Print a message with optional color.

        Args:
            message: The message to print
            color: ANSI color code (optional)
        """
        if color:
            print(color + message + Display.RESET_COLOR)
        else:
            print(Display.RESET_COLOR + message)

    @staticmethod
    def print_error(message: str):
        """Print an error message in red."""
        print('\033[1;31;40m' + message + Display.RESET_COLOR)

    @staticmethod
    def print_success(message: str):
        """Print a success message in green."""
        print('\033[1;32;40m' + message + Display.RESET_COLOR)

    @staticmethod
    def wait_for_input():
        """Wait for user to press enter."""
        input("\nPresione la tecla intro para continuar...")

    @staticmethod
    def get_integer_input(prompt: str, min_val: int = 1, max_val: int = 9) -> int:
        """
        Get integer input from user with validation.

        Args:
            prompt: The prompt to display
            min_val: Minimum valid value
            max_val: Maximum valid value

        Returns:
            Valid integer input
        """
        while True:
            try:
                value = int(input(Display.RESET_COLOR + prompt + "\n"))
                if min_val <= value <= max_val:
                    return value
                else:
                    Display.print_error(f"Debe ingresar un valor entre {min_val} y {max_val}.")
            except ValueError:
                Display.print_error(f"Sólo números enteros entre {min_val} y {max_val}.")

    @staticmethod
    def print_elimination(team: Team):
        """
        Print elimination message for a team.

        Args:
            team: The eliminated team
        """
        Display.clear()
        color = Display.COLORS[team]
        team_names = {
            Team.RED: "Rojo",
            Team.BLUE: "Azul",
            Team.YELLOW: "Amarillo",
            Team.GREEN: "Verde"
        }
        print(f"{color}El equipo {team_names[team]} ha sido eliminado.{Display.RESET_COLOR}\n")
        Display.wait_for_input()

    @staticmethod
    def print_winner(team: Team):
        """
        Print winner message for a team.

        Args:
            team: The winning team
        """
        Display.clear()
        Display.print_title()
        color = Display.COLORS[team]
        team_names = {
            Team.RED: "Rojo",
            Team.BLUE: "Azul",
            Team.YELLOW: "Amarillo",
            Team.GREEN: "Verde"
        }
        print(f"{color}¡FELICIDADES!{Display.RESET_COLOR}\n")
        print(f"{color}El equipo {team_names[team]} ha ganado el juego!{Display.RESET_COLOR}\n")
        Display.wait_for_input()
