from pytube import YouTube
from pytube import Playlist


link = input("Enter the playlist link: ")
pl = Playlist(link)

print("-----------------------------------------------------")
print(pl.title)
print("-----------------------------------------------------\n")


i = 1
c = ' '

"""
for video in pl.videos:
    print(f' [{c}]   {i}. {video.title}')
    i += 1


print("\n-----------------------------------------------------")
"""
id1, id2 = input("Enter the first and last video ID: ").split()
id1 = int(id1)
id2 = int(id2)

print("\n")

i = 1
down = False
for video in pl.videos:
    if i >= id1 and i <= id2:
        c = 'x'
        down = True
    else:
        c = ' '
        down = False

    print(f' [{c}]   {i}. {video.title}')
    if down:
        stream = video.streams.get_by_itag(22)
        print(f"          Resolution: 720p")
        print(f"          Size: {stream.filesize/(1024*1024)} MB")
        #video.streams.filter(progressive=True).get_highest_resolution().download()
    i += 1

