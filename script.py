'''
This script downloads the meta data from YouTube and writes it to a file.
'''
import bios
import youtube_dl

PLAYLIST = 'https://www.youtube.com/playlist?list=PLI1_CQcV71RmeydXo-5K7DAxLsUX6SVhL'

ydl_opts = {}

if __debug__:
    meta = bios.read('./meta.json')
else:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(PLAYLIST, download=False)

for entry in meta['entries']:
    print(entry['upload_date'])
    print(entry['title'])
    print(entry['webpage_url'])

bios.write('./meta.json', meta, file_type='json')
