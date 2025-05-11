import pandas as pd
import lyricsgenius

# Genius API ayarı
genius = lyricsgenius.Genius("K3bH5s0XNMkcDHjHL-bOihG0YWBHZkyqnIfsOgWDo54bx4GwehtHlbFtau7lU5G5")
genius.remove_section_headers = True
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]

# Excel'den oku
df = pd.read_csv("C:/Users/recep/Downloads/uzgun_600_sarki_temiz1.csv", encoding="utf-8-sig")

# Şarkı sözlerini çek
lyrics_list = []
for index, row in df.iterrows():
    try:
        song = genius.search_song(title=row["song_title"], artist=row["artist"])
        if song:
            lyrics_list.append({
                "artist": row["artist"],
                "song_title": row["song_title"],
                "lyrics": song.lyrics,
                "mood": row["mood"]
            })
            print(f"✅ {row['artist']} - {row['song_title']}")
        else:
            print(f"⚠️ Bulunamadı: {row['artist']} - {row['song_title']}")
    except Exception as e:
        print(f"❌ Hata: {row['artist']} - {row['song_title']} → {e}")

# Yeni veri çerçevesi oluştur
lyrics_df = pd.DataFrame(lyrics_list)

# CSV olarak düzgün formatta kaydet
lyrics_df.to_csv("C:/Users/recep/sarki_sozleri_dogru.csv", index=False, encoding="utf-8-sig")
print("🎉 Tamamlandı.")
