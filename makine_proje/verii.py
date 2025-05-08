import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# 🔐 API kimlik bilgilerin (BURAYA GERÇEK BİLGİLERİNİ KOY)
client_id = "02ac0f68fada457fa7311a78163255b9"
client_secret = "3f52cb8a1b57441f8249b76a74542031"

# 🎧 Spotify playlist URL'si (public bir liste)
playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6"  # Örnek: Türkçe Pop Günü
mood = "mutlu"

# Playlist ID'yi ayıkla
playlist_id = playlist_url.split("/")[-1].split("?")[0]

# API bağlantısı
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=30)

# Şarkıları çek
try:
    results = sp.playlist_items(playlist_id, additional_types=['track'], limit=100, market="TR")
except Exception as e:
    print("❌ Spotify'dan veri çekilirken hata oluştu:")
    print(e)
    exit()

tracks = results["items"]

# Devamı varsa çekmeye devam et
while results['next']:
    results = sp.next(results)
    tracks.extend(results["items"])

# Şarkıları işleyip kaydet
songs = []
for item in tracks:
    track = item['track']
    if track and track['name'] and track['artists']:
        songs.append({
            "artist": track['artists'][0]['name'],
            "song_title": track['name'],
            "mood": mood
        })

df = pd.DataFrame(songs)
df.to_csv(f"{mood}_sarkilar.csv", index=False, encoding="utf-8-sig")
print(f"✅ {len(df)} şarkı kaydedildi: {mood}_sarkilar.csv")
