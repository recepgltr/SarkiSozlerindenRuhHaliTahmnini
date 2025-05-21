import os
import pandas as pd

folder_path = r"C:\Users\recep\OneDrive\Masaüstü\öfke veri"
file_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

merged_df = pd.DataFrame()

for file in file_list:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path)

        # mood sütunu eksikse sabit olarak ekle
        if "mood" not in df.columns:
            df["mood"] = "öfke"

        if not df.empty:
            print(f"✔️ Yüklendi: {file} ({df.shape[0]} satır)")
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        else:
            print(f"⚠️ Boş dosya atlandı: {file}")
    except Exception as e:
        print(f"❌ Hata: {file} - {e}")

# Tekrarları sil
merged_df.drop_duplicates(subset=["artist", "song_title"], inplace=True)

# Kaydet
output_path = os.path.join(folder_path, "ofke_birlesik_temiz.csv")
if not merged_df.empty:
    merged_df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"✅ Kaydedildi: {output_path}")
else:
    print("❗ Uyarı: Hiçbir veri birleştirilemedi.")
