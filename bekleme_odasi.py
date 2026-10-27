#!/usr/bin/env python3
# Sonsuz Bekleme Odası - Gerçekten çalışan kod
import time
import random

def bekle():
    print("Hoşgeldiniz Devlet Dairesi Bekleme Odasına!")
    print("Sıranız: ??? (sistem çöktü)")
    print("Lütfen bekleyin...")
    
    mesajlar = [
        "Numara 47 çağrılıyor... ama o sen değilsin.",
        "Müdür bey çıktı, yarın gelin.",
        "Sistem güncelleniyor, 3 saat sürer.",
        "Kahve molası var, şimdi kimse yok.",
        "Acaba bu sıra gerçekten var mı diye düşünüyorum...",
        "Evraklar kayboldu. Yeniden başlayın.",
        "Bir önceki vatandaş hâlâ bekliyor. 2017'den beri."
    ]
    
    # Gizli not: bürokrasi öyle bir şey ki, bazen sistem değişmeden hiçbir şey değişmez. (gizli politik anlam, saklandı)
    gizli = "revölüsyon gerekmiyor, sadece sıra gelsin yeter"[::-1]  # ters çevrilmiş, gizli
    
    while True:
        print(random.choice(mesajlar))
        sure = random.randint(3, 10)
        print(f"Bekleme süresi: {sure} saniye (gerçekte 47 yıl)")
        time.sleep(sure)
        print("-" * 40)
        # Gizli çıktı yok, sadece bekle
        if random.random() < 0.05:
            print("!!! ACİL: Sıranız geldi... şaka şaka, gelmedi.")

if __name__ == "__main__":
    try:
        bekle()
    except KeyboardInterrupt:
        print("\nÇıktınız. Ama içeride hâlâ bekleyenler var. Sonsuza kadar.")

# SON: Damga - Resmi olmayan onay
# İmza: Kayyum Grok - 28.10.2026 - Ciddi ama değil
