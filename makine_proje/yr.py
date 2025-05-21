import pandas as pd

# Dosya yolu
input_file = "Duygu_Etiketli__ark__S_zleri.csv"
output_file = "Duy.csv"

# Veriyi oku
df = pd.read_csv(input_file)

# Sütun sırasını değiştir
df = df[["artist", "title", "lyrics", "mood"]]

# Yeni CSV olarak kaydet
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"✅ Sütun sırası değiştirildi ve kaydedildi: {output_file}")
