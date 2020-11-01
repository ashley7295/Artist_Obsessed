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
