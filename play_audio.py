# play_audio.py
import subprocess

def play(audio: str):
    """
        play an audio that received as string.
    """
    subprocess.run(
        ["ffplay", "-nodisp", "-autoexit", audio],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )