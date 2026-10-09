import os
import pandas as pd
import numpy as np


def process_medical_dataset(file_path: str) -> list:
    """
    Конвеєр обробки та мапінгу даних.
    Зчитує датасет з папки data, видаляє дублікати та формує готові до запису об'єкти
    """
    print(f"[Generator] Зчитування файлу {file_path}...")

    if not os.path.exists(file_path):
        print(f"[Generator] Помилка: Файл '{file_path}' не знайдено!")
        print("Переконайтеся, що ви запускаєте скрипт з кореневої папки проєкту, а файл лежить у папці 'data'.")
        return []

    df = pd.read_csv(file_path, low_memory=False)

    df = df.dropna(subset=['name']).drop_duplicates(subset=['name'])

    processed_records = []

    print(f"[Generator] Початок очищення та підготовки {len(df)} записів...")


    for _, row in df.head(1000).iterrows():
        uses = [str(row[col]) for col in [f'use{i}' for i in range(5)] if pd.notna(row.get(col))]

        side_effects = [str(row[col]) for col in [f'sideEffect{i}' for i in range(42)] if pd.notna(row.get(col))]

        substitutes = [str(row[col]) for col in [f'substitute{i}' for i in range(5)] if pd.notna(row.get(col))]

        action_class = str(row.get('Action Class', '')) if pd.notna(row.get('Action Class')) else ""
        full_description = f"Action: {action_class}. Uses: {', '.join(uses)}. Side Effects: {', '.join(side_effects)}."

        record = {
            "name": str(row['name']),
            "chemical_class": str(row.get('Chemical Class')) if pd.notna(row.get('Chemical Class')) else None,
            "therapeutic_class": str(row.get('Therapeutic Class')) if pd.notna(row.get('Therapeutic Class')) else None,
            "is_habit_forming": str(row.get('Habit Forming', 'No')).strip().lower() == 'yes',
            "substitutes": substitutes,
            "uses": uses,
            "side_effects": side_effects,
            "full_description": full_description,
            "price": round(np.random.uniform(50.0, 1500.0), 2)  # Програмна генерація комерційної ціни
        }
        processed_records.append(record)

    return processed_records


if __name__ == "__main__":
    print("[Generator Worker] Запуск процесу генерації навантаження...")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.dirname(current_dir)

    input_file = os.path.join(project_root, "data", "medicine_dataset.csv")

    cleaned_data = process_medical_dataset(input_file)

    if cleaned_data:
        print(f"[Generator Worker] Успішно підготовлено {len(cleaned_data)} записів.")
        print("[Generator Worker] Демонстрація першого запису:")
        print(f" - Назва: {cleaned_data[0]['name']}")
        print(f" - Ціна: {cleaned_data[0]['price']} грн")
        print(f" - Рецептурний: {'Так' if cleaned_data[0]['is_habit_forming'] else 'Ні'}")
        print(f" - Аналоги: {cleaned_data[0]['substitutes']}")
        print(f" - Текст для пошуку (фрагмент): {cleaned_data[0]['full_description'][:120]}...")