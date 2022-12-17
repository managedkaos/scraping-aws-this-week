import bios
import youtube_dl

playlist = 'https://www.youtube.com/playlist?list=PLI1_CQcV71RmeydXo-5K7DAxLsUX6SVhL'

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(playlist, download=False)

bios.write('./meta.json', meta, file_type='json')