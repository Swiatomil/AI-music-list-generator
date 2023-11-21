from JSON_list_generator import create_playlist
from spotify_conection import list_creator, list_of_title_to_IDs
import argparse

parser = argparse.ArgumentParser(description="simple comand line song utility")
parser.add_argument("-p", type=str, help="The prompt to describe the playlist")
parser.add_argument("-v", type=int, help='amount of songs that will be in playlist')
parser.add_argument("-n", type=str, help='name of the playlist')
args = parser.parse_args()

volume = args.v
prompt = args.p
name = args.n

Jlist = create_playlist(volume, prompt)
IDs = list_of_title_to_IDs(Jlist)
list_creator(name, IDs)


"songs to listening while driving for few hour with my girlfriend. she like have rock music. but we dont like really popular songs, and i wanna half of the song to be in polish language"

