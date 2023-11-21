import os

import spotipy
from dotenv import load_dotenv

load_dotenv(".env")


def list_creator(name: str, id_list):
    sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri="http://localhost:9999",
            scope="playlist-modify-private"
        )
    )

    cu = sp.current_user()

    sp_list = sp.user_playlist_create(
        cu["id"],
        public=False,
        name=name
    )
    sp.user_playlist_add_tracks(cu['id'], sp_list['id'], id_list)

def list_of_title_to_IDs(titles):

    sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri="http://localhost:9999",
            scope="playlist-modify-private"
        )
    )
    IDs=[]
    for title in titles:
        song_id = sp.search(q=title['title']+', '+title['artist'], type='track', limit=1)['tracks']['items'][0]['id']
        IDs.append(song_id)
    return IDs



