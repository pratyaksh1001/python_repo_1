import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
client_id = "b5cfd173bd9d4347ba233f589547ed14"
client_secret = "fa6043e904164dac8832cd6228b27f87"
rfak_url = "https://api.spotify.com/artist/3OLGltG8UPIea8sA4w0yg0"
token = {
  "access_token": "b5cfd173bd9d4347ba233f589547ed14",
  "token_type": "Bearer",
  "expires_in": 3600
}
connection = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=rfak_url)
print(connection.get_auth_response())
