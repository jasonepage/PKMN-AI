![gui](images/gui.PNG)

# PKMN-AI

PKMN-AI is an AI bot that automates the process of playing Pokemon. The script will observe the user's main output device and automatically begin playing the game. It utilizes computer vision to play through the game and recognize specific Pokemon encounters, which is beneficial for maintaining encounter metrics and data for shiny hunters.

# Features

- Option to customize the AI for different resoulutions and display settings.
- Works with a multitude of themes, fonts, and MODs.
- Stores encounter data for following sessions/restarts.
- Displays current encounters live on screen in a separate GUI window.

# Prerequisites

macOS/Windows 10+

> The script has only been tested on macOS and Windows 10 currently.

# Compatability & Expectations

> The AI must be able to recognize the HP (hit points) Bar on the screen to enter a counting state and track the encounter (no widgets or windows can block the HP Bar).

> The AI works best on fullscreen mode; however, the user can replace the 'hp_img.png' file with their needle image to recognize encounters.

# Installation

1. Download the latest version of the repository.
2. Install the required python modules by running the following command in your terminal for you virtual environment:

> $ pip install -r requirements.txt

3. Run main.py; create a shortcut if desired.

# Contact & Support
