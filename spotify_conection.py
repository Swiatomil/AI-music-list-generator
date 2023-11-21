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


if __name__ == "__main__":
    sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri="http://localhost:9999",
            scope="playlist-modify-private"
        )
    )
    song_id = sp.search(q='syn okiennika', type='track', limit=1)['tracks']['items'][0]['id']
    print(song_id)
    list_creator("aberracja", [song_id])