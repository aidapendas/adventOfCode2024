import pandas as pd
import numpy as np
import os


def is_ascending(l: list) -> bool:
    return all(
        l[i] < l[i + 1]
        and abs(l[i] - l[i + 1]) <= 3
        and abs(l[i] - l[i + 1]) >= 1
        for i in range(len(l) - 1)
    )


def is_descending(l: list) -> bool:
    return all(
        l[i] > l[i + 1]
        and abs(l[i] - l[i + 1]) <= 3
        and abs(l[i] - l[i + 1]) >= 1
        for i in range(len(l) - 1)
    )


def convert_to_numbers(str_list: list) -> list:
    return [int(x) for x in str_list]


def is_safe(l: list) -> bool:
    return is_ascending(l) or is_descending(l)


def is_safe_with_dampener(l: list) -> bool:

    for i in range(0, len(l)):
        l_aux = l.copy()
        l_aux.pop(i)
        if is_safe(l_aux):
            return True

    return False


dir_path = os.getcwd()

df_ = pd.read_excel(
    dir_path + "/adventOfCode2024/Day2/UnusualData.xlsx", sheet_name="Sheet1"
)

safety_list = [
    is_safe(convert_to_numbers(l.split(' '))) for l in df_["Reports"].tolist()
]

print(f"Number of reports that are safe: {safety_list.count(True)}")

safety_list_with_dampener = [
    (
        is_safe(convert_to_numbers(l.split(' ')))
        if is_safe(convert_to_numbers(l.split(' ')))
        else is_safe_with_dampener(convert_to_numbers(l.split(' ')))
    )
    for l in df_["Reports"].tolist()
]

print(
    f"Number of reports that are safe with dampener: {safety_list_with_dampener.count(True)}"
)
