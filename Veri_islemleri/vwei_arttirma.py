import pandas as pd
import random
import nltk
from nltk.corpus import wordnet

# Gerekli WordNet dosyalarını indir
nltk.download('wordnet')
nltk.download('omw-1.4')

# Synonym replacement fonksiyonları
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word, lang="eng"):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace("_", " ")
            if synonym.lower() != word.lower():
                synonyms.add(synonym)
    return list(synonyms)

def synonym_replacement(text, n=2):
    words = text.split()
    new_words = words.copy()
    random_word_list = list(set([word for word in words if get_synonyms(word)]))
    random.shuffle(random_word_list)
    num_replaced = 0

    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        if synonyms:
            synonym = random.choice(synonyms)
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        if num_replaced >= n:
            break

    return ' '.join(new_words)

# Veri setini oku
df = pd.read_csv("veri_son_hali.csv")
df = df[["clean_lyrics", "mood"]].dropna()

# Veri artırımı yap
df_augmented = df.copy()
df_augmented["clean_lyrics"] = df_augmented["clean_lyrics"].apply(lambda x: synonym_replacement(x, n=2))

# Orijinal ve artırılmış veriyi birleştir
df_combined = pd.concat([df, df_augmented], ignore_index=True)
df_combined.to_csv("veri_arttirilmis.csv", index=False)

print("✅ Veri artırımı tamamlandı. Kaydedilen dosya: veri_arttirilmis.csv")
