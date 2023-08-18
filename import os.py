import os

# Klasör yolu
klasor_yolu = 'dosya_klasoru/'

# Klasördeki dosyaları al
dosyalar = os.listdir(klasor_yolu)

# Aranacak kelime veya ifade
aranan_ifade = 'hedef_kelime'

# Dosyaları dolaş ve düzenle
for dosya_adı in dosyalar:
    dosya_yolu = os.path.join(klasor_yolu, dosya_adı)
    
    if dosya_adı.endswith('.txt'):  # Sadece metin dosyalarını düzenle
        with open(dosya_yolu, 'r') as dosya:
            icerik = dosya.read()
            
            if aranan_ifade in icerik:
                yeni_icerik = icerik.replace(aranan_ifade, 'yeni_kelime')
                
                with open(dosya_yolu, 'w') as yeni_dosya:
                    yeni_dosya.write(yeni_icerik)
                    
print('Düzenleme tamamlandı.')
