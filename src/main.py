from functions import download_audio, audio_process, download_video

yt_url = str(input("Video link = "))
request = int(input("Audio/Video => 1/2 = "))
if request == 1:
    download_audio(yt_url)
    audio_process(yt_url)
elif request == 2:
    download_video(yt_url)