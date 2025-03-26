# Vārdu Meistars (Wordfinder)

Šī ir tīmekļa lietotne, kas ļauj meklēt latviešu vārdus, balstoties uz pieejamajiem burtiem un zināmiem burtiem noteiktās vietās.

## Uzstādīšana

```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Atver pārlūkā: [http://localhost:5000](http://localhost:5000)

## Formāti:

- "letters" – pieejamie burti (piemēram: alite)
- "pattern" – zināmā forma ar "_" (piemēram: _a_i_)

---

## `tezaurs_words.txt` saturs

Failā `tezaurs_words.txt` ir vairāk nekā 75 tūkstoši latviešu valodas vārdu, apvienojot:

- LU MII publicētos atvērtos korpusa vārdus (lemmatizēti)
- `lv.hardwords` un līdzīgus projektus no GitHub
- Vārdi ir unikāli (bez dublikātiem), visi mazajiem burtiem, viens vārds katrā rindā

---

## Kā atjaunināt vārdnīcu?

1. Lejupielādē LU Korpusa vārdu sarakstu no [https://klas.lu.lv](https://klas.lu.lv) (meklē lemmu sarakstus).
2. Klonē `lv.hardwords` vai `latvian-wordlist.txt` no GitHub (meklē pēc šiem terminiem).
3. Apvieno failus:

```bash
cat fails1.txt fails2.txt | tr A-Z a-z | sort | uniq > tezaurs_words.txt
```

---

## Licences un autortiesības

Pārliecinies, ka izmantotie avoti atļauj lietošanu atbilstoši projekta vajadzībām.
