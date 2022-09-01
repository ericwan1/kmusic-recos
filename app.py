from flask import Flask, request, render_template
import pandas as pd
import joblib

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

client_id = ''
client_secret = ''

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Used to check the tokens and what not if they work
# results = sp.artist_albums("7n2Ycct7Beij7Dj7meI4X0", album_type='album', country='US')
# print(results)

# Loading the dataset
data = pd.read_csv('album_to_track_df.csv', header = 0).dropna()
track_data = data[['Track_Title'
                        , 'danceability'
                        , 'energy'
                        , 'loudness'
                        , 'speechiness'
                        , 'acousticness'
                        , 'instrumentalness'
                        , 'liveness'
                        , 'valence'
                        , 'tempo']].dropna()
track_data.index = track_data['Track_Title']
track_data = track_data.drop(['Track_Title'], axis = 1)

# Declare a Flask app
app = Flask(__name__)

# Running the app
if __name__ == '__main__':
    app.run(debug = True)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Unpickle classifier
        clf = joblib.load("nnbs.pkl")
        
        # Get values through input bars
        spotify_input = request.form.get("inputURL")

        # Sample song link, from mac client:
        # https://open.spotify.com/track/2oBMZYteeO8DyXV9gDx6Za?si=1ec2215522d64bc1
        # Sample possible link from web browser:
        # https://open.spotify.com/track/0skYUMpS0AcbpjcGsAbRGj 
        # Want to extract everything after 'track/' and before '?' if it exists
        try:
            sbstr_1 = spotify_input.split("/track/")[1]
            if '?' in sbstr_1:
                sp_pass_id = sbstr_1.split("?")[0].strip()
                proceed_check = True
            else:
                sp_pass_id = sbstr_1.strip()
                proceed_check = True
        except:
            print("invalid url - try copying the link directly from Spotify!")
            proceed_check = False
        
        if proceed_check:
            # Contains the 8 main metrics, time signature, length, key, urls, and other information needed
            track_features = sp.audio_features(sp_pass_id)
            track_features_df = pd.DataFrame(track_features)

            # Put inputs to audio only dataframe
            track_audio_only = track_features_df[['danceability',
                                                'energy', 
                                                'loudness', 
                                                'speechiness', 
                                                'acousticness', 
                                                'instrumentalness', 
                                                'liveness',
                                                'valence',
                                                'tempo']]
            track_audio_only['Track_Title'] = str(sp.track(track_features_df.iloc[0]['id'])['name'])
            track_audio_only.set_index('Track_Title', inplace = True)

            # Currently the shape is:
            # | danceability | energy | loudness | speechiness | acousticness | 
            # instrumentalness | liveness | valence | tempo |
            # With index of the track title name
            
            # Create dataframe to pass into clustering algorithm
            track_data_copy = track_data.copy()
            track_data_copy = track_data_copy.append(track_audio_only)
            
            # Clustering 
            rescaled_artist_data = StandardScaler().fit_transform(track_data_copy)
            nnbs = NearestNeighbors(n_neighbors = 11, algorithm = 'ball_tree').fit(rescaled_artist_data)
            distances, indices = nnbs.kneighbors(rescaled_artist_data)

            # Shaping outputs from clustering
            kmusic_nn_output = pd.DataFrame(indices)
            kmusic_nn_output['Track_Title'] = track_data_copy.index

            # Retrieving Track URLs from the data
            # This step is necessary to create our dictionary to match up tracks and artists
            # Adding artists to the final dataframe
            kmusic_nn_output['Track_Id'] = list(data[['Track_Id']]).append(spotify_input)
            # Getting user submitted artist information for incorporation into final dataframe
            # This step is necessary to create our dictionary to match up tracks and artists
            user_submitted_track_info_dict = sp.track(track_features_df.iloc[0]['id'])['artists'][0]
            user_submitted_artist_name = user_submitted_track_info_dict['name']
            user_submitted_artist_link = user_submitted_track_info_dict['external_urls']['spotify']
            # Adding artist names to the final dataframe
            kmusic_nn_output['Artist'] = list(data[['Artist']]).append(user_submitted_artist_name)
            # Adding Artist Ids to the final dataframe
            kmusic_nn_output['Artist_Id'] = list(data[['Artist_Id']]).append(user_submitted_artist_link)
            
            # Assembling dictionary for id - artist/track lookup for use in final recommendations
            keys = list(kmusic_nn_output.index)
            values = list(zip(kmusic_nn_output.Track_Title
                            , kmusic_nn_output.Track_Id
                            , kmusic_nn_output.Artist
                            , kmusic_nn_output.Artist_Id))
            t_id_t_title_dict = dict(zip(keys, values))

            preds_row = kmusic_nn_output.iloc[len(data)]

            for i in range(1,11):
                song_index = preds_row[i]
                recc_song_track_title = t_id_t_title_dict.get(song_index)[0]
                recc_song_track_id = t_id_t_title_dict.get(song_index)[1]
                recc_song_artist_name = t_id_t_title_dict.get(song_index)[2]
                recc_song_artist_id = t_id_t_title_dict.get(song_index)[3]

            
            # Figure what to do with outputs once you get there by fixing the html first

            predictions = "so far so good"

        # Return predictions
        return render_template("website.html", output = recc_song_track_title)

    else:
        # This is the default, as the default route is 'GET'
        prediction = "Enter a song link from Spotify!"
        return render_template("website.html", output = prediction)



