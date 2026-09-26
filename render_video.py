"""Renders heart.py offscreen into heart.mp4 (with music) for sharing."""
import os
import subprocess
import sys

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

import imageio_ffmpeg
import pygame

import heart

HERE = os.path.dirname(os.path.abspath(__file__))
SONG = next(p for p in (os.path.join(HERE, "love_you.mp3"),
                        os.path.join(os.path.dirname(HERE), "love_you.mp3"))
            if os.path.exists(p))
OUT = os.path.join(HERE, "heart.mp4")
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


class Done(BaseException):
    pass


pygame.init()
pygame.mixer.init()
seconds = min(pygame.mixer.Sound(SONG).get_length(), 45)
total = int(seconds * heart.FPS)

proc = subprocess.Popen(
    [FFMPEG, "-y", "-loglevel", "error",
     "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{heart.WIDTH}x{heart.HEIGHT}",
     "-r", str(heart.FPS), "-i", "-",
     "-i", SONG, "-map", "0:v", "-map", "1:a", "-t", f"{seconds:.2f}",
     "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium",
     "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT],
    stdin=subprocess.PIPE)

count = 0


def capture_flip():
    global count
    proc.stdin.write(pygame.image.tobytes(pygame.display.get_surface(), "RGB"))
    count += 1
    if count % 60 == 0:
        print(f"{count}/{total}", flush=True)
    if count >= total:
        raise Done


pygame.display.flip = capture_flip
heart.pygame.time.Clock = lambda: type("C", (), {"tick": lambda self, fps: None})()

try:
    heart.main()
except Done:
    pass
finally:
    proc.stdin.close()
    proc.wait()

print("saved", OUT)
sys.exit(proc.returncode)
