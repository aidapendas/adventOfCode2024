# 🎄 Advent of Code 2024 - Day 4: Ceres Search 🎄

In today’s challenge, we help a little Elf solve her unusual word search puzzle aboard the Ceres monitoring station. This isn't your typical word search; it's a puzzle where **"XMAS"** can appear in every direction, and in part two, we’re hunting for **X-MAS** patterns instead!

---

## 📜 Challenge Description

### Part 1: Finding All "XMAS"

The Elf’s word search puzzle allows the word "XMAS" to appear:

- Horizontally (forwards and backwards),
- Vertically (upwards and downwards),
- Diagonally (in all directions),
- Overlapping other words.

Your task is to count how many times "XMAS" appears in the puzzle.

**Example Input:**

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

**Output for Example:** `18` occurrences of "XMAS".

---

### Part 2: Finding All "X-MAS"

The Elf flips the puzzle, revealing that it’s not just a search for "XMAS" but for **X-MAS** patterns:

- An **X-MAS** is two instances of "MAS" arranged in an "X" shape.
- Each "MAS" can be written forwards or backwards.

**Example Input:**

```
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```


**Output for Example:** `9` occurrences of "X-MAS".

---

## 🛠️ Approach

### Part 1: Finding All "XMAS"

1. Parse the word search puzzle into a grid.
2. Search for "XMAS" in:
   - All rows (forwards and backwards).
   - All columns (upwards and downwards).
   - All diagonal directions.
3. Count all occurrences.

### Part 2: Finding All "X-MAS"

1. Use the same grid from Part 1.
2. Search for "MAS" patterns arranged in an "X" shape:
   - Top-left to bottom-right diagonal,
   - Top-right to bottom-left diagonal.
3. Each diagonal must contain two valid "MAS" patterns.

---

## 🛠️ Implementation

### Code Structure

- **`day04/solution.py`**: Python script containing the solutions for both parts.
- **`day04/input.txt`**: Puzzle input containing the corrupted memory.
- **`day04/README.md`**: Challenge description (this file).

---

## 🔍 How to Run

1. Ensure you have Python installed.
1. Place your input in day02/input.xlsx with one report per line.
3. Run the solution script:
   ```bash
   python solution.py
    ```

---

## 📝 License
This challenge and solution are part of the Advent of Code 2024 event and are shared under the MIT License.



