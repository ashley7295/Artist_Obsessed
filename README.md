#### ARTIST OBSESSED
#### Summary of the Program:

## This program uses 3 different API's to gather 3 different types of information about a musical artist and thier music for the user. The user will enter an Artists Name, an Album Title and a Song title, they will then get the artists follower count from Spotify, the album artwork for that album and lyrics to the song they requested. The User can also choose to save the information they searched for as a Bookmark and then look back on what they have bookmarked in the past. The user can search for a bookmark, delete a bookmark or view all bookmarks. 


## Quick start
### Generate spotify keys for Follower Count

1. Open [Spotify for developers](https://developer.spotify.com/documentation/). 
2. Go to "Dashboard".
3. Sign up if you're new, otherwise sign in
4. Create an app. Add title and description, check all boxes and hit create.
5. Copy `CLIENT ID` key.
6. Head towards your system's environment variables, create a new variable.
7. In the `Variable name` field write `SPOTIFY_CLIENT_ID` and in the `variable value` paste the "key" which you have just copied.
8. Copy `CLIENT SECRET` key from where you copied `CLIENT ID`.
9. Again create a new environment variable.
10.In the `Variable name` field write `SPOTIFY_CLIENT_SECRET` and in the `variable value` paste the "key" which you have just copied.

### Generate apiseeds key for Lyrics

1. Open [Apiseeds](https://apiseeds.com)
2. Go to `start now`.
3. Register if you're new, otherwise login.
4. Copy the key in "YOURAPIKEY" box.
5. Create a new environment variable.
6. In the `Variable name` field write `apiseeds_api_key` and in the `variable value` paste the "key" which you have just copied.

### Generate last.fm key for Cover Art

1. Open [Last.fm](https://www.last.fm/api)
2. Go to `Get an API account`.
3. Register if you're new, otherwise login.
4. Copy the key in "API KEY" in the details of your new API account.
5. Create a new environment variable.
6. In the `Variable name` field write `COVER_KEY` and in the `variable value` paste the "key" which you have just copied.


## Installation

1. Create a new virtual environment by running `virtualenv`.
2. Activiate your virtual environment by running `source {your virutal environment name}/bin/activate`
3. Install `requirements.txt` by running `pip install -r requirements.txt`
4. Create `.env` file in your project's root directory if not already created


## Screen Shots of the Program Functioning

# Program Starting - Main Menu
![Main Menu](https://user-images.githubusercontent.com/31251156/97811789-669e4600-1c42-11eb-9242-8e7cff0dd50f.png)

# Selecting Option 1 - Starting Search Querie
![Option 1 - Start Search](https://user-images.githubusercontent.com/31251156/97811905-2c817400-1c43-11eb-97fb-262f70f3ab13.png)

# Selecting Option 2 - Display All Bookmarks
![Option 2 - Display All Bookmarks](https://user-images.githubusercontent.com/31251156/97811948-8da94780-1c43-11eb-91f6-a70df8381bee.png)

