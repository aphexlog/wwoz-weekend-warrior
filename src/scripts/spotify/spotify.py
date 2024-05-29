# script to create playlist in spotify 

import json
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

keys = json.load(open('./credentials.json'))

os.environ['SPOTIPY_CLIENT_ID'] = keys['SPOTIPY_CLIENT_ID']
os.environ['SPOTIPY_CLIENT_SECRET'] = keys['SPOTIPY_CLIENT_SECRET']
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback/'

# Set up Spotify API credentials
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def generate_playlist():
 
    # Opening JSON file
    f = open('scripts/ai/response_data/combined_response.json')

    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    artists = []
    for i in data['Artists']:
        artists.append(i)

    # Closing file
    f.close()

    # Create empty list to store track IDs
    track_ids = []

    # Choose the number of songs to add to the playlist from the artist's top tracks (max 10)
    num_songs = 2

    # Loop through each artist and see if there is a match, if there is, get top tracks
    not_found = []
    for artist in artists:
        search = []
        results = sp.search(q=artist, type="artist")
        for r in results["artists"]["items"]:
                search.append(r["name"])
        
        print(search) 
        if any(artist in s for s in search):
            print('name found')

            if results["artists"]["items"]:
                artist_id = results["artists"]["items"][0]["id"]
                top_tracks = sp.artist_top_tracks(artist_id)
                if top_tracks["tracks"]:
                    for i in range(min(num_songs, len(top_tracks["tracks"]))):
                        try:
                            track_ids.append(top_tracks["tracks"][i]["id"])
                            print('adding ', top_tracks["tracks"][i]["id"], ' for artist ', artist)
                        except Exception as e:
                            print('Adding song failed: ')
                            print(e)
        else:
            print(f"Artist: '{artist}' not Found, skipping")
            not_found.append(artist)

    print(f"'{len(not_found)}' out of '{len(artists)}' artists not found:")
    print(not_found)

    # Create a new playlist and add the top 5 tracks from each artist
    playlist_name = "test-playlist-wwoz-v4"
    playlist = sp.user_playlist_create(user=sp.me()["id"], name=playlist_name)

    # Add tracks to playlist in batches of 100 (to help with large number of artists)
    for i in range(0, len(track_ids), 100):
        sp.playlist_add_items(playlist["id"], track_ids[i:i + 100])

    print(f"Playlist '{playlist_name}' created successfully with {len(track_ids)} tracks!")

generate_playlist()