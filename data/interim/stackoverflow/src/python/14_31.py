from pytube import Playlist
import os
import re

def download(playlist):
    progress = None
    PATH = f'./{title}'
    with open(PATH+'/dependList.txt','r') as f:
        progress = int(f.read())

    videos = playlist.videos
    for i,video in enumerate(videos):
        if i >= progress:
            v = video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
            v.download(PATH+'/')
            with open(PATH+'/dependList.txt','w') as f:
                f.write(f'{i+1}')
        print(f'Downloaded {i+1} video')

link = input('Enter link:')
pl = Playlist(link)
total_videos = len(pl.videos)
print(f'Total Videos:{total_videos}')
title = ' '.join(re.findall("[a-zA-Z]+", pl.title))
print(title)

if os.path.exists(title):
    length_file = len(os.listdir(title)) - 1
    if length_file!=total_videos:
        download(pl)
        print("DONE")
    else:
        print('Already Exist')
else:
    os.makedirs(f'./{title}')
    with open(f'./{title}/dependList.txt','w') as f:
        f.write('0')
    download(pl)
    print('DONE')
