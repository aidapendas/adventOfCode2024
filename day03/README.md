# 🎄 Advent of Code 2024 - Day 3: Mull It Over 🎄

On Day 3 of the Advent of Code, we face a corrupted memory issue while debugging a computer program at the North Pole Toboggan Rental Shop. The goal is to extract and compute valid multiplication instructions from corrupted memory data, and later, manage conditional instructions that enable or disable multiplications.

---

## 📜 Challenge Description

### Part 1: Multiplication Extraction

The corrupted memory contains jumbled-up instructions. Your task is to find all valid `mul(X,Y)` instructions, compute their results, and sum them up.

- **Valid Instructions**: `mul(X,Y)` where `X` and `Y` are integers (1-3 digits).
- **Invalid Characters**: Instructions with any extra characters (e.g., `mul[3,7]`, `mul(4*,`) are ignored.

**Example Corrupted Memory:**

```
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```

- Valid instructions:
  - `mul(2,4)` → 2 * 4 = 8
  - `mul(5,5)` → 5 * 5 = 25
  - `mul(11,8)` → 11 * 8 = 88
  - `mul(8,5)` → 8 * 5 = 40
- **Sum of Results**: 8 + 25 + 88 + 40 = **161**

---

### Part 2: Conditional Multiplications

In addition to `mul(X,Y)`, the memory now contains two new conditional instructions:

1. **`do()`**: Enables future `mul` instructions.
2. **`don't()`**: Disables future `mul` instructions.

Only the most recent `do()` or `don't()` applies to subsequent `mul` instructions. By default, `mul` instructions are enabled at the start.

**Example Corrupted Memory:**

```
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```


- Valid instructions under conditions:
  - `mul(2,4)` → Enabled → 8
  - `mul(5,5)` → Disabled (after `don't()`) → Ignored
  - `mul(11,8)` → Disabled → Ignored
  - `mul(8,5)` → Enabled (after `do()`) → 40
- **Sum of Results**: 8 + 40 = **48**

---

## 🧩 Input Format

The input is a single string containing the corrupted memory. It includes:

- Valid and invalid `mul(X,Y)` instructions.
- Conditional `do()` and `don't()` instructions.
- Other irrelevant characters and invalid sequences.

---

## 🚀 How to Solve

### Part 1: Extracting Valid Multiplications

1. Use a regular expression to find valid `mul(X,Y)` instructions.
2. Parse the integers `X` and `Y`, compute their product, and sum up all results.

### Part 2: Handling Conditional Instructions

1. Track the state of multiplication (enabled or disabled) using `do()` and `don't()` instructions.
2. Only compute results for valid `mul(X,Y)` instructions that are enabled under the current state.

---

## 🛠️ Implementation

### Code Structure

- **`day03/solution.py`**: Python script containing the solutions for both parts.
- **`day03/input.txt`**: Puzzle input containing the corrupted memory.
- **`day03/README.md`**: Challenge description (this file).

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


