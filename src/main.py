from functions import download_audio, audio_process, download_video


async def process_link(link, option):
    if option == "audio":
        await download_audio(link)
        audio_name = await audio_process(link)
        return audio_name
    elif option == "video":
        await download_video(link)
