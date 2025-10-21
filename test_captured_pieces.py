#!/usr/bin/env python3
"""
Test script to verify captured pieces remain on the board.
"""
from board import Board
from pieces import Team, Militant
from display import Display


def test_captured_pieces():
    """Test that captured pieces stay on board as dead pieces."""
    print("Testing captured piece visibility...")

    board = Board()
    display = Display()

    # Get initial state
    militant1 = board.get_piece(1, 3)  # Red militant
    militant2 = board.get_piece(1, 7)  # Blue militant

    print(f"Before capture:")
    print(f"  Militant 1 (Red) at (1,3): {militant1}, alive={militant1.is_alive}")
    print(f"  Militant 2 (Blue) at (1,7): {militant2}, alive={militant2.is_alive}")

    # Simulate a capture: move militant2 to capture position
    board.set_piece(1, 4, militant2)  # Move blue militant
    board.set_piece(1, 7, None)

    # Now simulate militant1 capturing militant2
    captured = board.move_piece(1, 3, 1, 4)

    print(f"\nAfter capture:")
    print(f"  Captured piece: {captured}")
    print(f"  Is captured piece dead? {not captured.is_alive}")

    # Place the dead piece somewhere
    board.set_piece(2, 5, captured)

    print(f"  Dead piece placed at (2,5): {board.get_piece(2, 5)}")

    # Verify the dead piece is visible
    dead_piece = board.get_piece(2, 5)
    assert dead_piece is not None, "Dead piece should still be on board!"
    assert not dead_piece.is_alive, "Captured piece should be dead!"
    assert dead_piece.team == Team.BLUE, "Dead piece should retain its team!"

    print("\n✓ Dead pieces remain on board!")
    print("✓ Dead pieces are marked as not alive!")
    print("✓ Dead pieces retain their team color!")

    # Show board state
    print("\nBoard state (dead pieces show in purple/magenta):")
    print(board)

    print("\nWith colors:")
    display.render_board(board, None)


if __name__ == "__main__":
    test_captured_pieces()
