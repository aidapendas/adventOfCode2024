import re
import os


def count_word_occurrences(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Down-right diagonal
        (1, -1),  # Down-left diagonal
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1),  # Up-left diagonal
        (-1, 1),  # Up-right diagonal
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def search(r, c, dr, dc):
        for i in range(word_length):
            nr, nc = r + i * dr, c + i * dc
            if not is_valid(nr, nc) or matrix[nr][nc] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search(r, c, dr, dc):
                    count += 1

    return count


# Read the word search from a text file
file_path = ("input.txt")  # Replace with the path to your file

with open(file_path, 'r') as file:
    word_search = [line.strip() for line in file.readlines() if line.strip()]


# Convert the word search into a matrix of characters
matrix = [list(row) for row in word_search]

# Word to search for
word = "XMAS"

# Count occurrences
count = count_word_occurrences(matrix, word)
print(f"The word '{word}' occurs {count} times.")

##### part 2 #####

def count_x_mas(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    patterns = ["MAS", "SAM"]  # MAS can be forward or backward
    count = 0

    # Function to check if indices are within bounds
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Check for X-MAS centered at (r, c)
    def is_x_mas(r, c):
        for pattern in patterns:
            # Top-left to bottom-right diagonal
            if (
                is_valid(r - 1, c - 1)
                and is_valid(r + 1, c + 1)
                and matrix[r - 1][c - 1] == pattern[0]
                and matrix[r][c] == "A"
                and matrix[r + 1][c + 1] == pattern[2]
            ):
                for reverse_pattern in patterns:
                    # Top-right to bottom-left diagonal
                    if (
                        is_valid(r - 1, c + 1)
                        and is_valid(r + 1, c - 1)
                        and matrix[r - 1][c + 1] == reverse_pattern[0]
                        and matrix[r][c] == "A"
                        and matrix[r + 1][c - 1] == reverse_pattern[2]
                    ):
                        return True
        return False

    # Iterate over each cell in the matrix
    for r in range(1, rows - 1):  # Avoid edges
        for c in range(1, cols - 1):  # Avoid edges
            if matrix[r][c] == "A" and is_x_mas(r, c):
                count += 1

    return count

file_path = ("input.txt")  # Replace with the path to your file

with open(file_path, 'r') as file:
    word_search = [line.strip() for line in file.readlines() if line.strip()]

# Convert the word search into a matrix of characters
matrix = [list(row) for row in word_search]

# Count occurrences of X-MAS
result = count_x_mas(matrix)
print(f"The X-MAS pattern occurs {result} times.")
