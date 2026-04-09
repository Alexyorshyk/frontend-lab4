# stats_module.py
# Модуль із підпрограмами для статистичної обробки показників

import statistics

def get_average(data_dict):
    if not data_dict:
        return None
    return sum(data_dict.values()) / len(data_dict)

def get_min(data_dict):
    if not data_dict:
        return None
    return min(data_dict.values())

def get_max(data_dict):
    if not data_dict:
        return None
    return max(data_dict.values())

def get_median(data_dict):
    if not data_dict:
        return None
    return statistics.median(data_dict.values())

def find_jumps(data_dict, threshold):
    jumps = []
    keys = list(data_dict.keys())
    for i in range(len(keys) - 1):
        v1 = data_dict[keys[i]]
        v2 = data_dict[keys[i + 1]]
        diff = abs(v2 - v1)
        if diff > threshold:
            jumps.append(
                f"{keys[i]} → {keys[i+1]}: {diff}"
            )
    return jumps

def show_table(data_dict, title):
    print(f"\n=== Таблиця показів: {title} ===")
    print("Мітка\tЗначення")
    for k, v in data_dict.items():
        print(f"{k}\t{v}")