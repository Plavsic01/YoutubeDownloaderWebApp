from pytube import YouTube
from pathlib import Path
import os


def download(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    downloads_path = str(Path.home() / "Downloads")
    down_file = video.download(output_path=downloads_path)
    base,ext = os.path.splitext(down_file)
    new_file = base + ".mp3"
    os.rename(down_file,new_file)

    return yt.title

