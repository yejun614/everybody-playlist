from yt_dlp import YoutubeDL

ydl_opts = {
    "format": "wav/beataudio/best",
    "outtmpl": "test",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "wav",
    }]
}

URLS = [
    ""  # youtube url
]

with YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
    print("error_code", error_code)
