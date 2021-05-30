import spotipy
import argparse
import json
import pandas as pd
from typing import Dict, List, Any
from spotipy.oauth2 import SpotifyClientCredentials

def load_json(file_path: str) -> Dict:
    with open(file_path) as read_from_file:
        data = json.load(read_from_file)
        return data

DECADES = ['year:1960-1969',
    'year:1970-1979',
    'year:1980-1989',
    'year:1990-1999',
    'year:2000-2009',
    'year:2010-2019',
    'year:2020-2029']

def make_track(track_name:str, id:str, album_name:str, artist_name:str, popularity:str, decade:str) -> Dict:
    return {
        'track_name': track_name,
        'id': id,
        'album_name': album_name,
        'artist_name': artist_name,
        'popularity': popularity,
        'decade': decade
    }

TRACKS = []

def get_first_year_from_decade(decade:str) -> str:
    span = decade.split(':')[1]
    first_year, last_year = span.split('-')
    return first_year

def get_tracks(decade: str, spotify_api:Any) -> List:
    tracks = []
    year = get_first_year_from_decade(decade)
    for i in range(0,1000, 50):
        track_results = spotify_api.search(q=decade, type='track', limit=50, offset=i)
        for i, t in enumerate(track_results['tracks']['items']):
            track = make_track(
                track_name =t['name'],
                id = t['id'],
                album_name = t['album']['name'],
                artist_name = t['artists'][0]['name'],
                popularity = t['popularity'],
                decade = year)
            tracks.append(track)
    return tracks

def get_audio_features(track_ids, spotify_api):
    all_audio_features = []
    for track_id in track_ids:
        spotify_audio_features = spotify_api.audio_features([track_id])[0]
        all_audio_features.append(spotify_audio_features)
    return all_audio_features

def songs_with_audio_features(credentials_path: str) -> None:
    credentials = load_json(credentials_path)
    SP = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id=credentials['client_id'],
                                                                                client_secret=credentials['client_secret']))
    for decade in DECADES:
        tracks = get_tracks(decade, SP)
        TRACKS.extend(tracks)
    df_with_songs = pd.DataFrame.from_records(TRACKS)

    genres = {}
    for track in TRACKS:
        first_call_genres = SP.search(q="artist:{}".format(track['artist_name']), type='artist')
        for genre in first_call_genres['artists']['items']:
            genres[genre['name'].replace("'", '"')] = [sub.replace("'", '"') for sub in genre['genres']]
    df_with_songs['genre'] = df_with_songs['artist_name'].map(genres)
    audio_features = get_audio_features(df_with_songs['id'], SP)
    df_with_audio_features = pd.DataFrame.from_records(audio_features)
    songs_with_audio_features = pd.merge(df_with_songs, df_with_audio_features, how='inner', on='id')
    songs_with_audio_features.to_csv("songs_with_audio_features.csv", sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Create a file with all tracks."
    )

    parser.add_argument(
        "--credentials_path",
        required=True,
        type=str,
        help="path to credentials")

    args = parser.parse_args()

    songs_with_audio_features(args.credentials_path)
