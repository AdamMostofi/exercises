<p align="center">
  <strong>🏋️ Daily Code Practice</strong><br>
  <em>4 exercises · 6 levels · 4 languages · every single day</em>
</p>

---

From syntax basics to algorithmic thinking. Python, SQL, TypeScript, Node.js.
Each day builds muscle memory. No skipping levels.

---

## 📚 Languages

| Language | Level 0 | How to run |
|----------|---------|-----------|
| **Python** | `python/level-00/` | `python python/level-00/ex001-hello.py` |
| **SQL** (SQLite) | `sql/level-00/` | `python sql/level-00/ex001-select-all.py` |
| **TypeScript** | `typescript/level-00/` | `npx tsx typescript/level-00/ex001-hello.ts` |
| **Node.js** | `nodejs/level-00/` | `node nodejs/level-00/ex001-hello.js` |

---

## 📈 Levels

| Level | Name | What you master | Est. lines |
|-------|------|----------------|-----------|
| **0** | Warm-up | Print, variables, basic math, string ops | 1–3 |
| **1** | Fundamentals | Conditionals, loops, `range()`, basic functions | 3–8 |
| **2** | Toolkit | Lists, dicts, comprehensions, multiple params | 5–15 |
| **3** | Logic | Multi-condition, nested loops, filtering, mapping | 10–25 |
| **4** | Mastery | Recursion, OOP, file I/O, error handling | 15–40 |
| **5** | Challenge | Algorithms, efficiency, multi-step problems | 25–60 |

---

## 🧭 Progression

- **Start at Level 0** in each language. Do not skip.
- **4 exercises per day** (any mix of languages). Push after each batch.
- **12 exercises per level** (3 days), then move to next.
- **Stuck >15 min** → ask for a hint. Say `"just show me"` for the full answer.

---

## 🚀 Quick Start

```bash
# Python — no setup needed
python python/level-00/ex001-hello.py

# SQL — no setup needed (sqlite3 built into Python)
python sql/level-00/ex001-select-all.py

# TypeScript — needs tsx
npm install -g tsx
tsx typescript/level-00/ex001-hello.ts

# Node.js — needs Node (already installed)
node nodejs/level-00/ex001-hello.js
```

---

## 🗺️ Structure

```
exercises/
├── python/          ← Python practice
│   └── level-00/
├── sql/             ← SQL queries (via Python + sqlite3)
│   └── level-00/
├── typescript/      ← TypeScript type system practice
│   └── level-00/
└── nodejs/          ← Node.js core API practice
    └── level-00/
```

---

## 📦 Setup (one time)

```bash
# Install tsx for TypeScript exercises
npm install -g tsx

# Create the GitHub repo
gh repo create daily-code-practice --public --push
```

---

## 📝 Exercise format

```python
"""
ex001 - Title

Task description here.

EXPECTED OUTPUT:
some output
"""

# Your code below:
```

```sql
-- For SQL exercises (embedded in Python runner):
query = "YOUR SQL HERE"

-- For TypeScript and Node.js:
// standard file with instructions at the top
```
