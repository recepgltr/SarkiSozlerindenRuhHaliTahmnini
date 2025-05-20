import pandas as pd

# Giriş ve çıkış dosya yolları
input_file = 'uzgun_temiz.csv'
output_file = 'uzgun_temiz_flat.csv'

# CSV dosyasını oku
df = pd.read_csv(input_file)

# lyrics sütunundaki satır sonlarını (newline) temizle
df['lyrics'] = df['lyrics'] + df['lyrics'].str.replace('\n', ' ')

# Yeni CSV dosyasına kaydet
df.to_csv(output_file, index=False, encoding='utf-8')

print("Temizleme tamamlandı, dosya kaydedildi:", output_file)
