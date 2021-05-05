# Referenced from https://sotiriskakanos.com/2017/08/05/using-spotifys-web-api-with-python/

#Import required libraries
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials

#Authorize API using credentials
client_credentials_manager = SpotifyClientCredentials(client_id='b86bcb98e728443e9a690bf58572f53e', client_secret='ed42ae66555c4b01b3ab988efc6c4219')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('rmnvd22tpuikmwf5yzzsgnu2t') #My User ID/Name

print(playlists)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']

        print("   %d %32.32s %s  %s" % (i, track['artists'][0]['name'], track['name'],track['preview_url']))

for playlist in playlists['items']:
        if playlist['owner']['id'] == 'rmnvd22tpuikmwf5yzzsgnu2t' and playlist['name']=='surprise':
            print(playlist['name'])
            print(playlist['external_urls']['spotify'])

            # webbrowser.open(playlist['external_urls']['spotify'])
            print('  total tracks', playlist['tracks']['total'])

            results = sp.user_playlist('rmnvd22tpuikmwf5yzzsgnu2t', playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)