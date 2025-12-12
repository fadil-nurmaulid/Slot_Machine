import pygame
import os
from utils.file_manager import get_path  # <— integrate with file manager

# Initialize mixer
pygame.mixer.init()

_bg_music = None

# ===============================
#        BACKGROUND MUSIC
# ===============================
def play_bgm(file_name, loop=True):
    """Play background music in loop."""
    global _bg_music

    # Use file_manager.get_path instead of os.path.join
    path = get_path("gui", "assets", "bgm", file_name)

    if os.path.exists(path):
        _bg_music = pygame.mixer.Sound(path)
        _bg_music.play(-1 if loop else 0)
    else:
        print(f"BGM file not found: {path}")

def stop_bgm():
    """Stop the background music."""
    global _bg_music
    if _bg_music:
        _bg_music.stop()

# ===============================
#          SOUND EFFECTS
# ===============================
def play_sfx(file_name):
    """Play a short sound effect once."""

    # Use file_manager.get_path for stable path
    path = get_path("gui", "assets", "sounds", file_name)

    if os.path.exists(path):
        sfx = pygame.mixer.Sound(path)
        sfx.play()
    else:
        print(f"SFX file not found: {path}")
