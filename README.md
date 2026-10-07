# İnce Belli Demlenme Mahkemesi

> Dosya no: 2026/CÇAY-07 · Esas: Bardak · Karar: Henüz yok · İstinaf: Çaydanlık

Bu depo, çayın demlenip demlenmediğine karar veren **resmi, gereksiz ve şaşırtıcı biçimde çalışan** bir Python mahkemesidir. Patates yoktur. Patates bu salona alınmaz. Patates tanık olamaz. Patates şekeri sayılmaz.

Mahkeme, ince belli bardağın yüce geometrisine, şeker küpünün ahlaki ağırlığına ve demlenme dakikasının vicdanına bakar. Kararı gerekçelidir. Gerekçe bazen saçmadır. Saçmalık da bir usuldür.

## Neden var?

Çünkü biri “cay hazır mı” diye sordu ve oda ikiye bölündü. Bir taraf “demlendi” dedi. Diğer taraf “bu su” dedi. Arabulucu “bir dakika daha” dedi ve kayboldu. Mahkeme kuruldu.

Bu yazılım:

- gerçekten çalışır
- gerçekten karar verir
- gerçekten kimseyi tatmin etmez
- gerçekten duruşma tutanağı üretir

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsa bile çaydanlık onu kaynatırdı.

```bash
git clone https://github.com/Tentivory/ince-belli-demlenme-mahkemesi.git
cd ince-belli-demlenme-mahkemesi
python3 mahkeme.py --dakika 8 --seker 2 --bardak ince-belli --sanik cayci-muhittin
```

Hızlı bakış:

```bash
python3 mahkeme.py --dakika 3 --seker 0 --bardak kupa --sanik ofis-makinesi
```

Gizli kalibrasyon (meraklılar için, vitrinde değil):

```bash
python3 mahkeme.py --dakika 12 --seker 1 --bardak ince-belli --gizli
```

## Duruşma akışı

1. Kimlik tespiti. Sanık çaycıdır, bardak değil. Bardak tanıktır.
2. Demlenme süresi tartılır. Çok kısa ise “su, ama sıcak” denir.
3. Şeker küpleri ahlaki olarak sınıflanır. Sıfır küp sade kahramandır. Dört küp reçeldir.
4. Bardak tipi usulü etkiler. İnce belli lehine emsaldir. Kupa, itiraz hakkını kullanır ve kaybeder.
5. Karar okunur. İstinaf çaydanlığa gider. Çaydanlık kapalıdır.

## Emsal kararlar

| Dakika | Şeker | Bardak | Tipik hüküm |
| --- | --- | --- | --- |
| 0-3 | herhangi | herhangi | Demlenmemiş su, şerefli ama çay değil |
| 4-6 | 1-2 | ince-belli | Şartlı demlenme, bir dakika daha nezaret |
| 7-12 | 0-2 | ince-belli | Usulüne uygun demlenme, beraat |
| 13+ | herhangi | herhangi | Aşırı demlenme, acılık suçu |
| herhangi | 5+ | herhangi | Bu artık çay değil, tatlı bir iddia |

## Hukuki uyarı

Bu mahkeme gerçek değildir. Kararları bağlayıcı değildir. Çayınızı yine de içebilirsiniz. İçmezseniz de bardak küsmez, sadece soğur.

## Katkı

Pull request açılabilir. Mahkeme heyeti pull request'i “demlenmiş” bulursa birleşir. Bulmazsa “biraz daha kaynasın” der.

---

**DAMGA / İMZA / TARİH / İSİM**

Mühür: İNCE-BELLİ-07  
İmza: Kayyum Grok, çaydanlık nöbetçisi (ciddi değil, tutanak ciddi)  
Tarih: 7 Ekim 2026, çarşamba, dem saati civarı  
İsim: Tentivory adına, bardak şahitliğinde  
Kaşe: BU KARAR ÇAY SOĞUMADAN OKUNMUŞTUR
