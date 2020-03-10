playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}
playlist['songs'].append({'title': 'song4', 'artist': ['Tamar'], 'duration':8.5})
x = 0
st=''
for song in playlist['songs']:
    if (song['duration'] > x):
        x=song['duration']
        st='..'.join(song['artist'])
print(st)
#finds max duration amd prints artist in a string in a string