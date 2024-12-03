# 🎄 Advent of Code 2024 - Day 2: Red-Nosed Reports 🎄

In the second challenge of Advent of Code 2024, we assist the engineers at the Red-Nosed Reindeer reactor by analyzing unusual safety data and determining how many reports are safe under specific criteria.

---

## 📜 Challenge Description

### Story

The Red-Nosed Reindeer reactor safety system is strict: it can only tolerate levels that are either gradually increasing or decreasing. The engineers need your help analyzing their reactor data, which consists of multiple reports. Your task is to determine which reports are safe.

---

### Rules for Safe Reports

A report is considered **safe** if:

1. The levels are either all increasing or all decreasing.
2. Any two adjacent levels differ by at least `1` and at most `3`.

For **Part Two**, the reactor safety system is enhanced by the **Problem Dampener**, which can tolerate a single bad level. This means:

- If removing one level from an unsafe report makes it safe, the report counts as safe.

---

### Example Input

Each line of the input contains a report with several levels:

```
7 6 4 2 1 1 2 7 8 9 9 7 6 2 1 1 3 2 4 5 8 6 4 4 1 1 3 6 7 9
```

---

### Example Analysis

#### Without Problem Dampener (Part 1)

- `7 6 4 2 1`: Safe (decreasing by 1-2).
- `1 2 7 8 9`: Unsafe (increase of 5 between 2 and 7).
- `9 7 6 2 1`: Unsafe (decrease of 4 between 6 and 2).
- `1 3 2 4 5`: Unsafe (mix of increasing and decreasing).
- `8 6 4 4 1`: Unsafe (`4 4` is neither increasing nor decreasing).
- `1 3 6 7 9`: Safe (increasing by 1-3).

**Safe Reports**: 2

#### With Problem Dampener (Part 2)

- `7 6 4 2 1`: Safe without removing any level.
- `1 2 7 8 9`: Unsafe, even after removing one level.
- `9 7 6 2 1`: Unsafe, even after removing one level.
- `1 3 2 4 5`: Safe by removing `3`.
- `8 6 4 4 1`: Safe by removing one `4`.
- `1 3 6 7 9`: Safe without removing any level.

**Safe Reports**: 4

---

## 🧩 Input Format

- The input consists of multiple reports, one per line.
- Each report contains a list of integers separated by spaces, representing the levels.

---

## 🚀 How to Solve

### Part 1: Without Problem Dampener

1. For each report:
   - Check if all levels are strictly increasing or strictly decreasing.
   - Ensure adjacent levels differ by at least `1` and at most `3`.

### Part 2: With Problem Dampener

1. For each report:
   - If the report is already safe, count it as safe.
   - Otherwise, remove each level one at a time and recheck the safety rules.
   - Count the report as safe if removing a single level makes it safe.

---

## 🛠️ Implementation

### Code Structure

- **`day02/solution.py`**: Python script containing the solutions for both parts.
- **`day02/input.xlsx`**: Puzzle input with the reports.
- **`day02/README.md`**: Challenge description (this file).

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

