# skipify
Always skip a list of artists in spotify if they end up being played

## how to run
* create spotify app, see https://developer.spotify.com/my-applications/
* whitelist `https://localhost/asd` as redirect url for your spotify application
* create `config.py`, see `config.py.example`
* run with `./skipify.py`
* your default browser opens to do the spotify oauth, you are redirected afterwards
* copy the url you were redirected to into the console and press enter

## requirements
* Python3
* spotipy (NOT the pip version, install from github)
