# Asteroid

A small Asteroids-style game built with Python and Pygame.

## Requirements

- Python 3.12 or newer
- uv

## Install Python

Install Python 3.12+ before running the game.

- macOS: install via Homebrew:
  - `brew install python`
- Linux: use your package manager, for example:
  - Ubuntu/Debian: `sudo apt install python3 python3-pip`
  - Fedora: `sudo dnf install python3`
- Windows: download and install Python from https://www.python.org/downloads/

Make sure `python --version` works in your terminal after installation.

## Install uv

`uv` is used to manage the project environment and dependencies.

Install it with one of the following methods:

- macOS/Linux:
  - `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows (PowerShell):
  - `irm https://astral.sh/uv/install.ps1 | iex`
- With pip:
  - `python -m pip install --user uv`

After installation, verify it works:

- `uv --version`

## Play the game

From the project root, run:

```bash
uv run main.py
```

This command will create the virtual environment if needed and run the game using the project dependencies.

If you want to install dependencies explicitly before starting, you can also run:

```bash
uv sync
```

Then launch the game with:

```bash
uv run main.py
```
