"""
Game class for Djambi.
Manages game state, turns, and player interactions.
"""
from typing import Optional, Tuple
from board import Board
from player import Player
from pieces import Team, PieceType, Assassin, Necromobile, Provocateur, Reporter
from display import Display


class Game:
    """Main game controller."""

    def __init__(self):
        self.board = Board()
        self.players = [
            Player(Team.RED),
            Player(Team.BLUE),
            Player(Team.YELLOW),
            Player(Team.GREEN)
        ]
        self.current_player_index = 0
        self.display = Display()

    def get_current_player(self) -> Player:
        """Get the current player."""
        return self.players[self.current_player_index]

    def next_turn(self):
        """Advance to the next player's turn, skipping eliminated players."""
        while True:
            self.current_player_index = (self.current_player_index + 1) % 4
            if not self.players[self.current_player_index].is_eliminated:
                break

    def check_eliminations(self):
        """Check if any players should be eliminated."""
        for player in self.players:
            if not player.is_eliminated:
                # Check if leader is dead
                if player.check_elimination(self.board):
                    self.display.print_elimination(player.team)

                # Check if leader is trapped
                elif self.board.is_leader_trapped(player.team):
                    # Kill the leader
                    for piece, row, col in self.board.get_team_pieces(player.team):
                        if piece.piece_type == PieceType.LEADER and piece.is_alive:
                            piece.kill()
                            player.eliminate()
                            self.display.print_elimination(player.team)
                            break

                # Check if no valid moves
                elif not self.board.has_valid_moves(player.team):
                    # Kill the leader (no moves = elimination)
                    for piece, row, col in self.board.get_team_pieces(player.team):
                        if piece.piece_type == PieceType.LEADER and piece.is_alive:
                            piece.kill()
                            player.eliminate()
                            self.display.print_elimination(player.team)
                            break

    def check_winner(self) -> Optional[Player]:
        """
        Check if there's a winner.

        Returns:
            The winning player, or None if no winner yet
        """
        active_players = [p for p in self.players if not p.is_eliminated]
        if len(active_players) == 1:
            return active_players[0]
        return None

    def select_piece(self) -> Tuple[int, int]:
        """
        Prompt player to select a piece to move.

        Returns:
            (row, col) of selected piece
        """
        current_team = self.get_current_player().team

        while True:
            row = self.display.get_integer_input(
                "Ingrese el número (en dígito) de la fila en la que se ubica la pieza que desea mover."
            )

            # Check if player has any pieces in this row
            has_piece_in_row = False
            for col in range(1, 10):
                piece = self.board.get_piece(row, col)
                if piece and piece.team == current_team and piece.is_alive:
                    has_piece_in_row = True
                    break

            if not has_piece_in_row:
                self.display.print_error("No tienes pieza en esa fila.")
                continue

            col = self.display.get_integer_input(
                "Ingrese el número (en dígito) de la columna en la que se ubica la pieza que desea mover."
            )

            piece = self.board.get_piece(row, col)

            # Validate selection
            if piece is None:
                self.display.print_error("No hay pieza en ese lugar.")
                continue

            if not piece.is_alive:
                self.display.print_error("No puedes seleccionar piezas capturadas.")
                continue

            if piece.team != current_team:
                self.display.print_error("Esa pieza no es de tu equipo.")
                continue

            # Check if piece has valid moves
            possible_moves = piece.get_possible_moves(self.board, row, col)
            if not possible_moves:
                self.display.print_error("La pieza seleccionada no tiene movimientos posibles.")
                continue

            return (row, col)

    def select_destination(self, piece, from_row: int, from_col: int) -> Tuple[int, int]:
        """
        Prompt player to select destination for piece.

        Args:
            piece: The piece being moved
            from_row: Starting row
            from_col: Starting column

        Returns:
            (row, col) of destination
        """
        # Show possible moves
        possible_moves = piece.get_possible_moves(self.board, from_row, from_col)
        self.display.render_board(self.board, self.get_current_player().team, possible_moves)

        while True:
            to_row = self.display.get_integer_input(
                "Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover su pieza seleccionada."
            )
            to_col = self.display.get_integer_input(
                "Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover su pieza seleccionada."
            )

            # Validate move
            if (to_row, to_col) not in possible_moves:
                self.display.print_error("Movimiento inválido. Intente de nuevo.")
                continue

            # Check if trying to capture piece from dead team
            target = self.board.get_piece(to_row, to_col)
            if target:
                target_player = None
                for p in self.players:
                    if p.team == target.team:
                        target_player = p
                        break
                if target_player and target_player.is_eliminated and target.is_alive:
                    self.display.print_error("No puedes capturar las piezas de un líder capturado.")
                    continue

            # Special check for militants and leader in center
            if piece.piece_type == PieceType.MILITANT:
                center_piece = self.board.get_piece(5, 5)
                if to_row == 5 and to_col == 5 and center_piece:
                    if center_piece.piece_type == PieceType.LEADER:
                        self.display.print_error("Los militantes no pueden capturar a un líder si este se encuentra en la casilla central.")
                        continue

            # Check if non-leader trying to move to center
            if piece.piece_type != PieceType.LEADER:
                if to_row == 5 and to_col == 5 and target is None:
                    self.display.print_error("Sólo el líder puede estar en la posición central.")
                    continue

            return (to_row, to_col)

    def handle_assassin_capture(self, assassin_start: Tuple[int, int],
                                 capture_pos: Tuple[int, int], captured_piece):
        """
        Handle assassin's special capture mechanic (swap positions).

        Args:
            assassin_start: Starting position of assassin
            capture_pos: Position where capture occurred
            captured_piece: The captured piece
        """
        # Assassin swaps position with captured piece
        # Move captured piece to assassin's starting position
        self.board.set_piece(assassin_start[0], assassin_start[1], captured_piece)

    def handle_necromobile_move(self, necro_pos: Tuple[int, int], target_pos: Tuple[int, int]):
        """
        Handle necromobile's special move (moving dead pieces).

        Args:
            necro_pos: Position of necromobile after move
            target_pos: Position of dead piece to move
        """
        dead_piece = self.board.get_piece(target_pos[0], target_pos[1])

        if dead_piece and not dead_piece.is_alive:
            while True:
                self.display.render_board(self.board, self.get_current_player().team)
                new_row = self.display.get_integer_input(
                    "Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza capturada."
                )
                new_col = self.display.get_integer_input(
                    "Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza capturada."
                )

                # Validate: must be empty and not center
                if self.board.get_piece(new_row, new_col) is not None:
                    self.display.print_error("Las piezas capturadas sólo pueden ocupar lugares vacíos.")
                    continue

                if new_row == 5 and new_col == 5:
                    self.display.print_error("Las piezas capturadas no pueden ocupar el centro.")
                    continue

                # Move the dead piece
                self.board.set_piece(target_pos[0], target_pos[1], None)
                self.board.set_piece(new_row, new_col, dead_piece)
                break

    def handle_provocateur_move(self, prov_pos: Tuple[int, int], target_pos: Tuple[int, int]):
        """
        Handle provocateur's special move (moving live enemy pieces).

        Args:
            prov_pos: Position of provocateur after move
            target_pos: Position of live enemy piece to move
        """
        enemy_piece = self.board.get_piece(target_pos[0], target_pos[1])

        if enemy_piece and enemy_piece.is_alive:
            while True:
                self.display.render_board(self.board, self.get_current_player().team)
                new_row = self.display.get_integer_input(
                    "Ingrese el número (en dígito) de la fila en la que se ubica la casilla a donde quiere mover la pieza enemiga."
                )
                new_col = self.display.get_integer_input(
                    "Ingrese el número (en dígito) de la columna en la que se ubica la casilla a donde quiere mover la pieza enemiga."
                )

                # Validate: must be empty and not center
                if self.board.get_piece(new_row, new_col) is not None:
                    self.display.print_error("Las piezas solo pueden moverse a lugares vacíos.")
                    continue

                if new_row == 5 and new_col == 5:
                    self.display.print_error("Las piezas no pueden moverse al centro (solo el líder).")
                    continue

                # Move the enemy piece
                self.board.set_piece(target_pos[0], target_pos[1], None)
                self.board.set_piece(new_row, new_col, enemy_piece)
                break

    def handle_reporter_turn(self, reporter_pos: Tuple[int, int]):
        """
        Handle reporter's special capture mechanic (capture adjacent, piece stays).

        Args:
            reporter_pos: Position of reporter
        """
        reporter = self.board.get_piece(reporter_pos[0], reporter_pos[1])

        # Check if there are adjacent pieces to capture
        capture_targets = reporter.get_capture_targets(self.board, reporter_pos[0], reporter_pos[1])

        if capture_targets:
            self.display.print_message("¿Desea capturar una pieza adyacente? (s/n)")
            choice = input().lower()
            if choice == 's':
                self.display.print_message("Piezas disponibles para capturar:")
                for i, (row, col) in enumerate(capture_targets):
                    piece = self.board.get_piece(row, col)
                    print(f"{i + 1}. {piece.piece_type.value} en ({row}, {col})")

                if len(capture_targets) == 1:
                    target_row, target_col = capture_targets[0]
                else:
                    choice_idx = self.display.get_integer_input(
                        "Seleccione el número de la pieza a capturar:",
                        min_val=1,
                        max_val=len(capture_targets)
                    )
                    target_row, target_col = capture_targets[choice_idx - 1]

                # Capture the piece (it stays in place but is marked dead)
                captured = self.board.get_piece(target_row, target_col)
                if captured:
                    captured.kill()
                    self.display.print_success(f"Pieza {captured.piece_type.value} capturada!")

    def execute_move(self, from_row: int, from_col: int, to_row: int, to_col: int):
        """
        Execute a move and handle special piece mechanics.

        Args:
            from_row: Starting row
            from_col: Starting column
            to_row: Destination row
            to_col: Destination column
        """
        piece = self.board.get_piece(from_row, from_col)
        target = self.board.get_piece(to_row, to_col)

        # Special handling for different piece types
        if isinstance(piece, Assassin) and target:
            # Assassin swaps with captured piece
            captured = self.board.move_piece(from_row, from_col, to_row, to_col)
            if captured:
                self.handle_assassin_capture((from_row, from_col), (to_row, to_col), captured)

        elif isinstance(piece, Necromobile) and target and not target.is_alive:
            # Necromobile moves dead piece
            self.board.move_piece(from_row, from_col, to_row, to_col)
            self.handle_necromobile_move((to_row, to_col), (to_row, to_col))

        elif isinstance(piece, Provocateur) and target and target.is_alive:
            # Provocateur moves live enemy piece
            self.board.move_piece(from_row, from_col, to_row, to_col)
            self.handle_provocateur_move((to_row, to_col), (to_row, to_col))

        elif isinstance(piece, Reporter):
            # Reporter moves normally, then can capture adjacent
            self.board.move_piece(from_row, from_col, to_row, to_col)
            self.handle_reporter_turn((to_row, to_col))

        else:
            # Normal move/capture
            captured = self.board.move_piece(from_row, from_col, to_row, to_col)
            if captured:
                self.display.print_success(f"Pieza {captured.piece_type.value} capturada!")

    def play_turn(self):
        """Execute a single turn for the current player."""
        current_player = self.get_current_player()

        # Render board
        self.display.render_board(self.board, current_player.team)

        # Select piece to move
        from_row, from_col = self.select_piece()
        piece = self.board.get_piece(from_row, from_col)

        # Select destination
        to_row, to_col = self.select_destination(piece, from_row, from_col)

        # Execute move
        self.execute_move(from_row, from_col, to_row, to_col)

    def run(self):
        """Main game loop."""
        # Show instructions
        self.display.print_instructions()
        self.display.print_piece_guide()

        # Game loop
        while True:
            # Check for eliminations
            self.check_eliminations()

            # Check for winner
            winner = self.check_winner()
            if winner:
                self.display.print_winner(winner.team)
                break

            # Play turn
            self.play_turn()

            # Next turn
            self.next_turn()


if __name__ == "__main__":
    game = Game()
    game.run()
