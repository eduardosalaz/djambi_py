#!/usr/bin/env python3
"""
Djambi - A strategic board game for 4 players.

Refactored version with clean OOP design.
Run this file to start the game.
"""
from game import Game


def main():
    """Main entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
