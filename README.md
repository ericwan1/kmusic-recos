# kmusic-recos

Currently a Work in Progress.

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

### To Do:
- Complete recommendation engine