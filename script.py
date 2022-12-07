import youtube_dl
import bios

options = {
    'skip_download': True,
    'restrictfilenames': True,
    'noplaylist': True,
    'writeinfojson': True,
    'writethumbnail': True,
    'outtmpl': "%(id)s"
}

urls = bios.read('urls.yaml')

for video_url in urls:
    print(video_url)

    video_id = video_url.split('=')[1]

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_url])

    video = bios.read(f"{video_id}.info.json")

    print(video)
