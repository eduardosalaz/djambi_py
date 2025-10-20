# Djambi - Refactored Version

A strategic board game for 4 players, implemented in Python with clean object-oriented design.

## What Changed?

This is a **complete refactoring** of the original `DjambiFinal.py`. The code has been restructured from a single 3740-line procedural file with arithmetic encoding to a clean, modular, object-oriented design.

### Before (Original)
- ❌ Single 3740-line file
- ❌ Arithmetic encoding (pieces as 3-digit numbers like `511`)
- ❌ Massive code duplication (same logic repeated for 4 players)
- ❌ No separation of concerns
- ❌ Difficult to maintain and extend

### After (Refactored)
- ✅ Modular architecture (6 files, ~1000 lines total)
- ✅ Clean OOP design with proper classes
- ✅ Piece inheritance hierarchy
- ✅ Separation of concerns (Game, Board, Display, etc.)
- ✅ Easy to maintain and extend
- ✅ No code duplication

## Architecture

```
djambi.py           - Main entry point
game.py             - Game controller and turn management
board.py            - Board state and piece positions
pieces.py           - Piece classes with movement logic
player.py           - Player/team management
display.py          - Terminal rendering and UI
DjambiFinal.py      - Original implementation (preserved)
```

### Class Structure

**Pieces** (with inheritance):
- `Piece` (base class)
  - `Militant` - Moves max 2 squares
  - `Leader` - Moves max 8 squares, can occupy center
  - `Assassin` - Moves max 8 squares, swaps with captured piece
  - `Necromobile` - Moves max 8 squares, can move dead pieces
  - `Reporter` - Moves max 8 squares, captures adjacent only
  - `Provocateur` - Moves max 8 squares, can move live enemy pieces

**Core Classes**:
- `Board` - Manages 9x9 grid and piece positions
- `Player` - Tracks team state and elimination
- `Game` - Main game controller and turn logic
- `Display` - Handles terminal rendering with ANSI colors

## Installation & Running

### Original Version
```bash
python DjambiFinal.py
```

### Refactored Version
```bash
python djambi.py
```

Both versions play the same game with identical rules!

## Features

- ✅ 4-player strategic gameplay
- ✅ 6 unique piece types with special abilities
- ✅ ANSI color terminal display
- ✅ Input validation
- ✅ Turn-based gameplay
- ✅ Automatic elimination detection
- ✅ No external dependencies

## Game Rules

**Objective:** Capture all enemy leaders using your pieces.

**Pieces:**
- **Militante (M):** Move 1-2 squares, can't capture leader in center
- **Líder (L):** Move 1-8 squares, only piece allowed in center (5,5)
- **Asesino (A):** Move 1-8 squares, swaps position with captured piece
- **Necromóvil (N):** Move 1-8 squares, can relocate dead pieces
- **Reportero (R):** Move 1-8 squares, captures adjacent pieces only
- **Provocador (P):** Move 1-8 squares, can relocate live enemy pieces

**Elimination:** Lose your leader = eliminated from game

**Victory:** Last team with a living leader wins!

## Code Comparison

### Original Encoding
```python
# Piece encoded as 3-digit number: XYZ
# X = piece type (1-6)
# Y = team color (1-4)
# Z = status (1=alive, 0=dead)
tablero[1][1] = 511  # Leader, Red, Alive
pieza = int(tablero[x][y]/100)
color = int((tablero[x][y]%100)/10)
status = int(tablero[x][y]%10)
```

### Refactored Design
```python
# Clean OOP with enums and classes
from pieces import Leader, Team

leader = Leader(Team.RED)
print(leader.team)        # Team.RED
print(leader.is_alive)    # True
print(leader.piece_type)  # PieceType.LEADER
```

## Benefits of Refactoring

1. **Readability:** Code is self-documenting with clear class/method names
2. **Maintainability:** Easy to fix bugs and add features
3. **Testability:** Each class can be unit tested independently
4. **Extensibility:** Adding new pieces or rules is straightforward
5. **No Duplication:** Movement logic defined once per piece type
6. **Type Safety:** Enums prevent invalid states
7. **Separation of Concerns:** Display, logic, and state are separated

## Development

The refactored version maintains 100% feature parity with the original while being:
- **73% less code** (3740 lines → ~1000 lines)
- **6x more modular** (1 file → 6 files)
- **∞ more maintainable** (arithmetic logic → OOP)

## License

Same as original project.

## Credits

Original implementation: [eduardosalaz](https://github.com/eduardosalaz/djambi_py)
Refactoring: Clean code architecture following SOLID principles
