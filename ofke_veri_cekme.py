import pandas as pd
import os

# Dosya adları
dosyalar = ['mutlu_duzgun.csv', 'uzgun_duzgun.csv', 'ofke_duzgun.csv','Duy.csv','test_seti_donusmus.csv']

# CSV'leri oku ve birleştir
veriler = [pd.read_csv(dosya) for dosya in dosyalar]
birlesik_df = pd.concat(veriler, ignore_index=True)

# Sonucu kaydet
birlesik_df.to_csv('birlesik_veri.csv', index=False)
print("Birleştirme tamamlandı. Kaydedilen dosya: birlesik_veri.csv")
