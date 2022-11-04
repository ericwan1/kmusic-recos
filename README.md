# kmusic-recos

When I first began working on this project I wanted to see if there were any commonalities between my favorite artists and songs within k-pop. The scope slowly grew bigger and bigger over the months. Now, not only has data been scraped and a recommender system built, but a micro framework using flask has also been constructed for users to interact with the recommender engine. 

### How to Use This Repo

In order to run the "website" on your end, see the following steps:
1. First clone the repo to a desired location: `git clone https://github.com/ericwan1/kmusic-recos.git`
2. Open terminal or command prompt and navigate to the repository. 
3. Run `export FLASK_APP=app` or `set FLASK_APP=app` if you are using the latter.
4. Then run `flask run`. 
5. Following the output from step 4, you will notice that the framework is most likely running on the default port (5000). Follow the url provided `http://127.0.0.1:5000` and you can begin playing around with the site!

### Data Dictionary

- `273_kArtists.csv` contains 273 artists and their Spotify IDs
    * `Artist` (Artist Name)
    * `Spotify_Id` (Artists' Unique Spotify ID)
- `album_to_track_df.csv` houses artist, album, and track information
    * `Artist` (Artist Name)
    * `Artist_Id` (Artists' Unique Spotify ID)
    * `Album_Name` (Album Name)
    * `Album_Id` (Album's Unique Spotify ID)
    * `Track_Title` (Title of the Track)
    * `Track_Id` (A Track's Unique ID)
    * misc. song information – see bottom of dictionary
- `artist_appears_on_df.csv` contains information on other albums the artist appears on
    * `Artist` (Artist Name)
    * `Artist_Id` (Artists' Unique Spotify ID)
    * `Appears_On_Name` ("Albums" the Artist has Appeared On)
    * `Appears_On_Id` (The ID of the "Album" the Artist Appeared On)
- `compilation_track.csv` includes artist information and compilation information, as well as track information for tracks contained within the artist compilation
    * `Artist` (Artist Name)
    * `Artist_Id` (Artists' Unique Spotify ID)
    * `Compilation_Name` (Compilation Name)
    * `Compilation_Id` (The Compilation's Unique Spotify ID)
    * `Track_Title` (Title of the Track)
    * `Track_Id` (A Track's Unique ID)
    * misc. song information – see bottom of dictionary
- `single_album_track_data.csv` contains artist information, any "single albums" and tracks contained within said albums and track information
    * `Artist` (Artist Name)
    * `Artist_Id` (Artists' Unique Spotify ID)
    * `Single_Album_Name` (Name of the Single Album)
    * `Single_Album_Id` (Artists' Unique Spotify ID)
    * `Track_Title` (Title of the Track)
    * `Track_Id` (A Track's Unique ID)
    * misc. song information – see bottom of dictionary
- misc. song information 
    * `danceability` (Track Suitability to Dancing, 0.0 to 1.0)
    * `energy` (Measurement of Intensity and Activity, 0.0. to 1.0)
    * `key` (The Key of the Track – see pitch class table [Guide Here](https://en.wikipedia.org/wiki/Pitch_class))
    * `loudness` (Overall Loudness in Decibels, Typically -60 to 0 db) 
    * `mode` (Major or Minor, 1 or 0)
    * `speechiness` (Presence of Words – the higher, the more wordy. 0.0 to 1.0)
    * `acousticness` (Confidence Measurement of a Track Being Acoustic. 0.0 to 1.0)
    * `instrumentalness` (Predicts if a Track Contains no Vocals, 0.0 to 1.0)
    * `liveness` (Predicts if a Live Audience in the Track, 0.0 to 1.0)
    * `valence` (Musical Positiveness, the Higher, the 'Happier'. 0.0 to 1.0)
    * `tempo` (Track's Estimated BPM)
    * `duration_ms` (Track Duration in Milliseconds)
    * `time_signature` (Time Signature, 3 to 7 for 3/4 to 7/4)

### Future To Do's:
- Host everything on a server and make the website interactable to the world
- Automate the scraping notebook and orchestrate runs; potentially store and run everything in the cloud
