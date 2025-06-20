# Push Picasso

🎨 **Push Picasso** - GitHub Contribution Graph művészet generátor

Kreatív alkotásokat készíthetsz a GitHub contribution graph-odra szövegek és alakzatok kombinálásával!

## 🌟 Funkciók

- 📝 **Szöveg kiírás** - 5x4-es betűtípussal
- 🎨 **Alakzatok rajzolása** - 5x5-ös méretben (szív, csillag, emoji-k)
- 🔄 **Kombinált art** - Szöveg és alakzatok keverése
- 🗑️ **Art adatok törlése** - Biztonságos commit history tisztítás
- 🎯 **Moduláris felépítés** - Objektumorientált kód szerkezet

## 🚀 Használat

### 1. Indítás
```bash
python push_picasso.py
```

### 2. Menü opciók

**1. 🎨 Art létrehozása**
- Egyszerű prompt: "Mit írjunk ki?"
- Támogatja szöveg és alakzatok keverését
- Példa: `Hello "heart" World` → Hello ❤️ World

**2. 👀 Elérhető alakzatok**
- Az összes alakzat megjelenítése előnézettel
- Használati utasítások

**3. 🗑️ Art adatok törlése**
- Biztonságos helyi adatok törlése
- Git history tisztítás az art_data mappából

**4. 🚪 Kilépés**
- Program bezárása

## 🎨 Alakzatok használata

Alakzatok beszúrásához használd a `"alakzat_név"` formátumot:

```
Hello "heart" World
"star" Welcome "smiley"
Happy "diamond" Coding
```

### Elérhető alakzatok:
- `heart` - ❤️ Szív alakzat
- `star` - ⭐ Csillag alakzat  
- `smiley` - 😊 Mosolygó arc
- `diamond` - 💎 Gyémánt alakzat

## 📁 Fájlstruktúra

```
push-picasso/
├── push_picasso.py          # Fő alkalmazás
├── core/                    # Moduláris komponensek
│   ├── __init__.py
│   ├── git_handler.py       # Git műveletek
│   ├── layout_manager.py    # Elrendezés kezelés
│   ├── shape_renderer.py    # Alakzatok rajzolása
│   └── text_renderer.py     # Szöveg kiírás
├── patterns/                # Minták tárolása
│   ├── __init__.py
│   ├── alphabet.py          # Betű minták
│   └── shapes.py           # Alakzat minták
├── art_data/               # Generált commit fájlok
├── requirements.txt        # Függőségek
└── README.md              # Dokumentáció
```

## ⚙️ Technikai részletek

### Méretkonvenció
- **Szövegek**: 5 magas × 4 széles
- **Alakzatok**: 5 magas × 5 széles

### Git működés
- Minden pixel = 1 commit az adott napon
- Dátum-alapú commit generálás
- art_data/ mappában tárolódnak a commit fájlok

### Biztonságos adattörlés
A 3. menüpont biztonságosan törli az art adatokat:
- Csak az `art_data/` mappa törlése
- Git history tisztítás az art commit-okból
- A program forráskódja érintetlen marad

## 🎯 Példa művek

### Egyszerű szöveg
```
Input: "Hello"
Output: HELLO szöveg a contribution graph-on
```

### Szöveg alakzattal
```
Input: "Love "heart" Code"
Output: Love ❤️ Code a contribution graph-on
```

### Több alakzat
```
Input: ""star" GitHub "diamond""
Output: ⭐ GitHub 💎 a contribution graph-on
```

## 📋 Követelmények

- Python 3.6+
- Git telepítve és beállítva
- GitHub account

## 🔧 Telepítés

1. Repository klónozása:
```bash
git clone <repository-url>
cd push-picasso
```

2. Program futtatása:
```bash
python push_picasso.py
```

3. GitHub feltöltés:
```bash
git remote add origin <your-github-repo-url>
git push -u origin main
```

## 🤝 Hozzájárulás

Szívesen fogadok új alakzatokat, funkciókat és javításokat! Kérlek, kövesd az alábbi szabályokat:

### 📋 Hozzájárulási szabályok

#### 💻 Kód hozzájárulások
1. **Objektumorientált stílus**: Tartsd be a meglévő OOP struktúrát
2. **Magyar kommentek**: Dokumentáció és kommentek magyarul
3. **Moduláris felépítés**: Új funkciókat a megfelelő core/ modulban helyezd el
4. **Hibakezelés**: Mindig adj hozzá megfelelő try-catch blokkokat

#### 🧪 Tesztelési követelmények
1. **Alapfunkciók**: Teszteld minden menüpontot
2. **Alakzatok**: Ellenőrizd az új alakzatok megjelenését
3. **Hibakezelés**: Próbálj ki érvénytelen bemeneteket
4. **Git műveletek**: Teszteld a commit generálást

### 🔄 Hozzájárulási folyamat

1. **Fork**: Készíts fork-ot a repository-ból
2. **Branch**: Hozz létre új branch-et (`feature/uj-alakzat`)
3. **Fejlesztés**: Valósítsd meg a változtatásokat
4. **Tesztelés**: Teszteld alaposan a módosításokat
5. **Commit**: Írj értelmezhető commit üzeneteket magyarul
6. **Pull Request**: Küldj PR-t részletes leírással

### ✅ Pull Request követelmények

**Kötelező elemek:**
- 📝 Részletes leírás magyarul
- 🎯 Mi változott és miért
- 🧪 Tesztelési lépések leírása
- 📷 Képernyőképek (ha releváns)

**Commit üzenet formátum:**
```
[TÍPUS]: Rövid leírás magyarul

Részletes leírás a változtatásról...
```

**Típusok:**
- `[ALAKZAT]`: Új alakzat hozzáadása
- `[BETŰ]`: Új betű/karakter hozzáadása  
- `[FUNKCIÓ]`: Új funkció implementálása
- `[JAVÍTÁS]`: Hibajavítás
- `[DOKUMENTÁCIÓ]`: Dokumentáció frissítése

### 🚫 Nem fogadható hozzájárulások

- ❌ Nem 5x5-ös vagy 5x4-es minták
- ❌ Helytelen formátumú kód
- ❌ Angol kommentek/dokumentáció
- ❌ A meglévő API törése
- ❌ Teszteletlen kód
- ❌ Nem követi a projekt stílusát

**Kapcsolatfelvétel:**
Ha kérdésed van, nyiss GitHub Issue-t vagy írj részletes PR leírást!

## 📄 Licenc

MIT

---

**Push Picasso** - Tedd művészetté a GitHub contribution graph-od! 🎨✨ 