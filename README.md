## Installation

1. Create a new virtual environment by running `virtualenv`.
2. Activiate your virtual environment by running `source {your virutal environment name}/bin/activate`
3. Install `requirements.txt` by running `pip install -r requirements.txt`

## Obtain MusixMatch API KEY
1. Sign up for Musix Match api key here - https://developer.musixmatch.com/
   
2. Obtain your applicaion key from your dashboard https://developer.musixmatch.com/admin/applications

3. Create `.env` file in your project's root directory and add the api key to the file in this format `musix_api_key = 0000000000000000000000000` where the `0s` represent your applicatoin key 