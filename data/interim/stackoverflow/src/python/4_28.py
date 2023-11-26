import yt_dlp # pip install yt_dlp

def hook(d):
    if d['status'] == 'finished':
        filename = d['filename']
        print(filename) # Here you will see the PATH where was saved.

def client(video_url, download=False):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         return ydl.extract_info(video_url, download=download)

ydl_opts = { 
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s', # You can change the PATH as you want
        'download_archive': 'downloaded.txt',
        'noplaylist': True,   
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [hook]
}
