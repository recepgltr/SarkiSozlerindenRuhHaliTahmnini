import pandas as pd
import re

# 🔧 Türkçe harfleri İngilizce'ye çeviren fonksiyon
def turkish_to_english(text):
    return text.translate(str.maketrans("çğıöşü", "cgiosu"))

# 🧼 Temizleme fonksiyonu (işaretler, tekrarlar, özel karakterler)
def clean_lyrics(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()

    # "Contributors" + "Lyrics" kalıntılarını temizle
    text = re.sub(r"\d+\s*contributors.*?lyrics", "", text)

    # [verse], [chorus] gibi blok etiketlerini kaldır
    text = re.sub(r"\[.*?\]", "", text)

    # Noktalama ve özel işaretleri temizle
    text = re.sub(r"[\"“”‘’´`.,!?;:()\[\]\-—•]", "", text)

    # Satır tekrarlarını sil
    lines = text.split("\n")
    seen = set()
    unique_lines = []
    for line in lines:
        line = line.strip()
        if line and line not in seen:
            seen.add(line)
            unique_lines.append(line)

    # Satırları birleştir
    cleaned = " ".join(unique_lines)

    # Boşlukları sadeleştir
    cleaned = re.sub(r"\s+", " ", cleaned)

    return cleaned.strip()

# 📄 CSV dosyasını oku
df = pd.read_csv("genius_3000_turkce_sarki.csv")

# ✅ 1. Türkçe karakterli temizlik
df_turkce = df.copy()
df_turkce["lyrics_clean"] = df_turkce["lyrics"].apply(clean_lyrics)
df_turkce = df_turkce[df_turkce["lyrics_clean"].str.split().str.len() > 20]
df_turkce.to_csv("genius_3000_clean_turkce.csv", index=False, encoding="utf-8-sig")
print("✅ Türkçe karakterli temizlik tamamlandı.")

# ✅ 2. İngilizce karakterli ASCII versiyonu
df_ascii = df_turkce.copy()
df_ascii["lyrics_clean_ascii"] = df_ascii["lyrics_clean"].apply(turkish_to_english)
df_ascii = df_ascii.drop(columns=["lyrics_clean"])
df_ascii.to_csv("genius_3000_clean_ascii.csv", index=False, encoding="utf-8-sig")
print("✅ ASCII versiyon dosyası oluşturuldu.")
