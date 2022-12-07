import youtube_dl
import bios

ydl_opts = {
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

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    video = bios.read(f"{video_id}.info.json")

    print(f"## {video['upload_date']} - {video['title']}")

    for chapter in video['chapters']:
        print(f"- {chapter['title']}")
