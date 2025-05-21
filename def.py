import pandas as pd
import re

# Dosya yolları
input_path = "ofke.csv"
output_path = "ofke_duzgun.csv"

# CSV dosyasını oku
df = pd.read_csv(input_path)

# lyrics sütununu temizle
def clean_lyrics(text):
    if pd.isna(text):
        return ""
    
    text = str(text)
    
    # Satır sonlarını boşlukla değiştir
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    
    # "Contributors" ve "Lyrics" gibi gereksiz metinleri kaldır
    text = re.sub(r'\d+ Contributors', '', text)
    text = re.sub(r'\bLyrics\b', '', text, flags=re.IGNORECASE)
    
    # Fazla boşlukları sadeleştir
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# lyrics sütununa uygula
if 'lyrics' in df.columns:
    df['lyrics'] = df['lyrics'].apply(clean_lyrics)
elif 'temiz_lyrics' in df.columns:
    df['temiz_lyrics'] = df['temiz_lyrics'].apply(clean_lyrics)

# Yeni CSV olarak kaydet
df.to_csv(output_path, index=False, encoding='utf-8')
print(f"Temizleme tamamlandı. Kaydedilen dosya: {output_path}")
