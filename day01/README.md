# 🎄 Advent of Code 2024 - Day 1: Historian Hysteria 🎄


Welcome to the first challenge of Advent of Code 2024: **Historian Hysteria**. In this challenge, we assist the Elvish Senior Historians in reconciling two lists of historically significant locations to track down the missing Chief Historian!

---

## 📜 Challenge Description

### Story

The Chief Historian is missing, and with Christmas quickly approaching, the Elves need your help to locate him! Using lists of historically significant locations found in his office, your task is to reconcile two groups’ interpretations of the notes and calculate the following:

1. **Part 1**: The total distance between the two lists, pairing numbers by ascending order.
2. **Part 2**: A similarity score based on how often numbers in the left list appear in the right list.

---

### Example Input

Given two lists of numbers (location IDs):

  Left List: 3, 4, 2, 1, 3, 3 
  Right List: 4, 3, 5, 3, 9, 3


### Part 1: Total Distance

Pair numbers by ascending order:

- Pair smallest left (`1`) with smallest right (`3`), distance: `2`.
- Continue until all numbers are paired.

**Result**: Sum of all distances = `11`.

### Part 2: Similarity Score

For each number in the left list, calculate how often it appears in the right list:

- Multiply the number by its occurrence count.
- Sum the results for all numbers in the left list.

**Result**: Similarity score = `31`.

---

## 🧩 Input Format

- Two lists of integers: **Left List** and **Right List**.
- Each list represents location IDs from the Chief Historian's notes.

---

## 🚀 How to Solve

### Part 1: Total Distance

1. Sort both lists in ascending order.
2. Pair numbers from the smallest to largest.
3. Calculate the absolute difference for each pair and sum them up.

### Part 2: Similarity Score

1. For each number in the left list, count how many times it appears in the right list.
2. Multiply the number by its occurrence count.
3. Sum all these values to get the similarity score.

---

## 🛠️ Implementation

### Code Structure

- **`day01/solution.py`**: Python script containing the solutions for both parts.
- **`day01/input.xlsx`**: Puzzle input with the two lists of numbers.
- **`day01/README.md`**: Challenge description (this file).

---

## 🔍 How to Run

1. Ensure you have Python installed.
2. Place your input in day01/input.xlsx as two lists of integers.
3. Run the solution script:
  ```bash
  python solution.py
  ```

---

## 📝 License
This challenge and solution are part of the Advent of Code 2024 event and are shared under the MIT License.
