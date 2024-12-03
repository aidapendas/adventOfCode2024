import os
import re


def mul(a: int, b: int) -> int:
    return a * b


dirpath = os.getcwd()

with open(dirpath + '/input.txt', 'r') as file:
    content = file.read()

pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(pattern, content)

final_result = 0

for m in matches:
    x = int(m.split(',')[0].split('(')[1])
    y = int(m.split(',')[1].split(')')[0])
    final_result += mul(x, y)

print(f"Final result: {final_result}")
