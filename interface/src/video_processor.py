from yt_dlp import YoutubeDL


def download_video(url: str, dir: str) -> None:
    """
    Download video from youtube and puts it in directory from config

    Args:
        url (str): video url
        dir (str): destination dir
    """
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
    }
    with YoutubeDL(params=ydl_opts) as ydl:
        ydl.download(url_list=[url])
