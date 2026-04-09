# lab02_main.py
# Основна програма (варіант "Фітнес-браслет")

import stats_module as sm

def parse_input(input_str):
    try:
        return [float(x) for x in input_str.split()]
    except ValueError:
        print("Помилка: введено нечислові дані")
        return None

def create_data_dict(pulse, steps, calories):
    data = {
        "pulse": {},
        "steps": {},
        "calories": {}
    }
    for i in range(len(pulse)):
        label = f"T{i+1}"
        data["pulse"][label] = pulse[i]
        data["steps"][label] = steps[i]
        data["calories"][label] = calories[i]
    return data

def process_measurements(title, data_dict, threshold):
    sm.show_table(data_dict, title)
    print(f"Середнє: {sm.get_average(data_dict):.2f}")
    print(f"Мінімум: {sm.get_min(data_dict)}")
    print(f"Максимум: {sm.get_max(data_dict)}")
    print(f"Медіана: {sm.get_median(data_dict)}")

    jumps = sm.find_jumps(data_dict, threshold)
    if jumps:
        print("Різкі перепади:")
        for j in jumps:
            print(j)
    else:
        print("Різких перепадів не виявлено")

def main():
    print("=== Обробка даних фітнес-браслета ===")

    pulse = parse_input(input("Введіть пульс (уд/хв): "))
    steps = parse_input(input("Введіть кроки: "))
    calories = parse_input(input("Введіть калорії (ккал): "))

    if not pulse or not steps or not calories:
        return

    data = create_data_dict(pulse, steps, calories)

    process_measurements("Пульс", data["pulse"], 30)
    process_measurements("Кроки", data["steps"], 500)
    process_measurements("Калорії", data["calories"], 50)

if __name__ == "__main__":
    main()