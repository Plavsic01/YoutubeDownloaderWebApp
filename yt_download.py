from pytube import YouTube
from io import BytesIO


def download(url):
    yt = YouTube(url)
    buffer = BytesIO()
    video = yt.streams.filter(only_audio=True).first()
    video.stream_to_buffer(buffer=buffer)
    buffer.seek(0)
    return yt.title,buffer
