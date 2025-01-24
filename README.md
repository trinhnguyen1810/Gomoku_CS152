# Gomoku AI

An AI implementation of the Gomoku (Five in a Row) game using minimax algorithm with alpha-beta pruning.

## Features

- AI vs Human gameplay
- AI vs AI mode
- AI vs Random player mode
- 15x15 game board
- Efficient move generation using proximity heuristics
- Configurable search depth
- Win detection for horizontal, vertical, and diagonal lines

## Implementation

- Minimax algorithm with alpha-beta pruning
- Heuristic evaluation function based on sequence lengths and openings
- Search space optimization using stone proximity
- Depth-limited search with cutoff evaluation

## Requirements

- Python 3.x
- Virtual environment

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

```bash
python3 gomoku_game.py
```

## Testing Results

- AI consistently wins against random move generator (100/100 games)
- Competitive performance against human players
- Draw results in AI vs AI matches due to optimal play
