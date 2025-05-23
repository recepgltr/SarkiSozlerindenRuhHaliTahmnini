import lyricsgenius
import pandas as pd
import time

# 🔑 Buraya kendi Genius API anahtarını gir
genius = lyricsgenius.Genius("wCe3Tt4zwPHHmAt5rsamc8yPjVzYcCSkDvPFnyz30fNrNC8rHQr7gNLzaWoguNzE")

# 🔧 Önerilen ayarlar
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)", "(Demo)", "(Version)"]
genius.remove_section_headers = True
genius.timeout = 10

# 🎤 3000+ şarkı için geniş Türk sanatçı listesi
artist_names = [
    "Sezen Aksu", "Tarkan", "Barış Manço", "Ajda Pekkan", "Kenan Doğulu",
    "Sertab Erener", "Teoman", "Mor ve Ötesi", "Athena", "Duman",
    "Nil Karaibrahimgil", "Yalın", "Zeynep Bastık", "Fikret Kızılok", "MFÖ",
    "Levent Yüksel", "Emre Aydın", "Şebnem Ferah", "Göksel", "Ayna",
    "Candan Erçetin", "İzel", "Feridun Düzağaç", "Halil Sezai", "Mabel Matiz",
    "Berkant", "Mavi Sakal", "Gripin", "Seksendört", "Badem",
    "Cem Karaca", "Edip Akbayram", "Mazhar Alanson", "Edis",
    "Ezginin Günlüğü", "Bülent Ortaçgil", "Yaşar", "Tuğba Yurt", "Ziynet Sali",
    "Gökhan Türkmen", "Funda Arar", "Haluk Levent", "Demet Akalın", "İbrahim Tatlıses"
]

all_songs = []

for artist_name in artist_names:
    print(f"\n🎤 {artist_name} için şarkılar toplanıyor...")
    try:
        artist = genius.search_artist(artist_name, max_songs=100, sort="title")
        if artist:
            for song in artist.songs:
                all_songs.append({
                    "artist": artist.name,
                    "song_title": song.title,
                    "lyrics": song.lyrics,
                    "mood": ""  # Etiketleme için boş bırakıldı
                })
            print(f"✅ {artist.name} için {len(artist.songs)} şarkı alındı.")
        else:
            print(f"⚠️ {artist_name} bulunamadı.")
    except Exception as e:
        print(f"❌ Hata: {artist_name} → {e}")
    time.sleep(1)  # Rate limit koruması

# 💾 CSV’ye kaydet
df = pd.DataFrame(all_songs)
df.to_csv("genius_3000_turkce_sarki.csv", index=False, encoding="utf-8-sig")
print(f"\n✅ Toplam {len(all_songs)} şarkı başarıyla kaydedildi.")
