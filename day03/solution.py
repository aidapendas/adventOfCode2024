import os
import re


def mul(a: int, b: int) -> int:
    return a * b

def extract_enabled_multiplications(content):
    # Find the first occurrence of do() or don't()
    first_do_dont = re.search(r"do\(\)|don't\(\)", content)
    
    if not first_do_dont:
        return content  # No do() or don't() found, return the whole content

    # Extract everything before the first do() or don't()
    before_first_do_dont = content[:first_do_dont.start()]

    # Extract everything after each do() and before the next don't()
    between_do_dont = re.findall(r"do\(\)(.*?)(?:don't\(\)|$)", content, re.DOTALL)

    # Combine the results
    result = before_first_do_dont + ''.join(between_do_dont)
    return result


dirpath = os.getcwd()

with open(dirpath + '/input.txt', 'r') as file:
    content = file.read()

# Extract the valid instructions
enabled_multiplications = extract_enabled_multiplications(content)

pattern_mul = r'mul\(\d{1,3},\d{1,3}\)'
valid_mul = re.findall(pattern_mul, enabled_multiplications)

enabled_mul_result = 0

for m in valid_mul:
    x = int(m.split(',')[0].split('(')[1])
    y = int(m.split(',')[1].split(')')[0])
    enabled_mul_result += mul(x, y)

print(f'Enabled multiplications result: {enabled_mul_result}')
