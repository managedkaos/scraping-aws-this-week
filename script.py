import youtube_dl
import bios

ydl_opts = {
    'quiet': True,
    'skip_download': True,
    'restrictfilenames': True,
    'noplaylist': True,
    'writeinfojson': True,
    'writethumbnail': True,
    'outtmpl': "%(id)s"
}

urls = bios.read('urls.yaml')

for video_url in urls:

    video_id = video_url.split('=')[1]

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # TODO: Update the script to use in memory data vs reading the video details from a local file
    video = bios.read(f"{video_id}.info.json")

    print(f"## {video['upload_date']} - {video['title']}")
    print(f"   {video_url}")

    if 'chapters' in video:
        for chapter in video['chapters']:
            print(f"- {chapter['title']}")
    else:
        print('No chapters found for video.')
    
    print();
