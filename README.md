# scraping-aws-this-week
Scraping AWS this week with [youtube-dl](https://github.com/ytdl-org/youtube-dl)

- [Embedding youtube-dl](https://github.com/ytdl-org/youtube-dl#embedding-youtube-dl)
- [Options](https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312)
- Scrape metadata

        # TODO: Change this to use Python3 syntax
        import youtube_dl

         ydl_opts = {}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info('https://www.youtube.com/watch?v=9bZkp7q19f0', download=False) 

        print 'upload date : %s' %(meta['upload_date'])
        print 'uploader    : %s' %(meta['uploader'])
        print 'views       : %d' %(meta['view_count'])
        print 'likes       : %d' %(meta['like_count'])
        print 'dislikes    : %d' %(meta['dislike_count'])
        print 'id          : %s' %(meta['id'])
        print 'format      : %s' %(meta['format'])
        print 'duration    : %s' %(meta['duration'])
        print 'title       : %s' %(meta['title'])
        print 'description : %s' %(meta['description'])
