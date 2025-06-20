# 🎨 Push Picasso

Ez a Python program lehetővé teszi egyedi minták, alakzatok és szövegek rajzolását a GitHub contribution graph-ba automatikus git commit-ok generálásával. Az alkalmazás támogatja az inline alakzatok használatát a szövegben.

## ✨ Funkciók

- 📝 **Szöveg kiírása** (1 vagy 2 soros) inline alakzatokkal
- ❤️ **Alakzatok rajzolása** (szív, csillag, mosoly, gyémánt)
- 🎨 **Kombinált art létrehozás** szöveg + alakzatok egyszerre
- 🤖 **Automatikus git commit generálás** megfelelő dátumokkal
- 👀 **Mintaelőnézet** a konzolban
- 📅 **Dátum-alapú pozicionálás**
- 🎯 **Automatikus középre igazítás** (opcionális manuális pozicionálás)
- 🗑️ **Repository tisztítás** (helyi és GitHub teljes törlés)

## 🚀 Telepítés és használat

### 1. Repository klónozása/letöltése
```bash
git clone <repository-url>
cd push-picasso
```

### 2. Python futtatása
```bash
python push_picasso.py
```

### 3. Követd a menü utasításait
A program egyszerű menüt kínál:
- **Art létrehozása** - szöveg + alakzatok kombinálva
- **Elérhető alakzatok** megtekintése  
- **Lokális törlés** - helyi commit-ok törlése
- **GitHub törlés** - teljes repository tisztítás
- **Kilépés**

## 📋 Használati példák

### Art létrehozása (szöveg + alakzatok)
```
1. Válaszd az "1" opciót
2. Hány soros szöveget szeretnél? (1-2): 2
3. 1. sor: HELLO "heart" WORLD
4. 2. sor: "star" GITHUB "diamond"
5. Automatikus pozicionálás és rajzolás
```

### Inline alakzatok használata
A szövegben `"alakzat"` formátumban írd be az alakzatokat:
- `HELLO "heart" WORLD` - szív a szöveg közepén
- `"star" CODE ART "diamond"` - csillag elején, gyémánt végén
- `GITHUB "smiley"` - mosolygó a szöveg végén

### Elérhető alakzatok megtekintése
```
1. Válaszd a "2" opciót
2. Megtekintheted az összes alakzat előnézetét
```

### Repository tisztítás
```
Lokális tisztítás:
1. Válaszd a "3" opciót
2. Erősítsd meg: "i"

GitHub teljes tisztítás:
1. Válaszd a "4" opciót  
2. GitHub URL beállítása (ha szükséges)
3. Erősítsd meg: "i"
```

## 🎯 Elérhető alakzatok

Az inline használatra elérhető alakzatok:

- **"heart"** ❤️ - Szív alakzat
- **"star"** ⭐ - Csillag
- **"smiley"** 😊 - Mosolygó arc  
- **"diamond"** 💎 - Gyémánt

### Inline alakzatok használata
Az alakzatokat a szövegbe ágyazva használhatod:
```
Példák:
- HELLO "heart" WORLD
- "star" GITHUB
- CODE "smiley" ART "diamond"
```

Az alakzatok automatikusan felismerésre kerülnek és a szöveg részeként kerülnek elhelyezésre a GitHub contribution graph-ban.

## ⚙️ Működés

1. **Grid System**: A GitHub contribution graph 53 hét x 7 nap rácsos rendszer
2. **Dátum számítás**: A program automatikusan kiszámítja a megfelelő dátumokat
3. **Commit generálás**: Minden rajzolt ponthoz 1-4 commit készül a megfelelő dátummal
4. **Git repository**: Automatikusan inicializálja a git repo-t, ha szükséges

## 📁 Fájl struktúra

```
push-picasso/
├── push_picasso.py   # Fő program
├── requirements.txt  # Python függőségek (üres, csak stdlib)
├── README.md         # Ez a fájl
└── art_data/         # Automatikusan generált commit fájlok
```

## ⚠️ Fontos megjegyzések

1. **GitHub szinkronizálás**: A program csak helyi git commit-okat hoz létre
2. **Feltöltés**: A végén fel kell tölteni GitHub-ra: `git push origin <branch-név>`
3. **Dátum korlátok**: Csak múltbeli dátumokra lehet commit-ot készíteni
4. **Grid méret**: Maximum 53 hét x 7 nap (GitHub limit)

## 🔧 Testreszabás

A `push_picasso.py` fájlban könnyen módosítható:
- **Betű minták** (`get_alphabet_patterns()`) - új betűk hozzáadása
- **Alakzat minták** (`get_shape_patterns()`) - új alakzatok létrehozása  
- **Commit intenzitás** (1-4 közötti értékek) - színek sötétsége
- **Pozicionálás algoritmus** (`_place_inline_elements()`) - elrendezés logika
- **Parsing szabályok** (`parse_text_with_shapes()`) - inline alakzat felismerés

## 💡 Tippek

- **Inline alakzatok**: Használj `"alakzat"` formátumot a szövegben
- **Kombinációk**: Vegyíts szöveget és alakzatokat kreativitásért
- **Előnézet**: Nézd meg az elérhető alakzatokat a 2. menüpontban
- **Tisztítás**: Használd a GitHub törlést a teljes újrakezdéshez
- **Biztonsági kérdések**: `i` = igen, `n` = nem (gyors válaszadás)

## 🤝 Közreműködés

Ha új funkciót vagy javítást szeretnél hozzáadni:
1. Fork-old a repository-t
2. Készítsd el a módosításokat
3. Küldj pull request-et

---

**Készítette**: Push Picasso by [@ErikFisherGitHub](https://github.com/ErikFisherGitHub)  
**Nyelv**: Python 3.6+  
**Licence**: MIT 