def parse_record(line: str) -> dict:
    
    parts = line.split(";")
    
    # 1. Полей не ровно три -> ошибка
    if len(parts) != 3:
        raise ValueError("Некорректное количество полей в строке.")
        
    city, temp_str, date = parts
    
    # 2. Город или дата пустые -> ошибка
    if not city.strip() or not date.strip():
        raise ValueError("Название города или дата не могут быть пустыми.")
        
    # 3. Температура не число -> перехватываем ошибку float и кидаем свою
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура должна быть числом.")
        
    # ИСПРАВЛЕНО: Ключ изменен с "temp" на "temperature" по требованию тестов
    return {"city": city.strip(), "temperature": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> list[dict]:

    records = []
    
    for line in lines:
        # Пустые строки пропускаются молча
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            # Ошибочные строки пропускаются, не роняя программу
            pass
    return records


def average_by_city(records: list[dict]) -> dict:

    city_temps = {}
    
    for record in records:
        city = record["city"]
        # ИСПРАВЛЕНО: Ключ изменен с "temp" на "temperature"
        city_temps.setdefault(city, []).append(record["temperature"])
        
    return {city: round(sum(temps) / len(temps), 1) for city, temps in city_temps.items()}


def warmest_city(records: list[dict]) -> str:

    avg_temps = average_by_city(records)
    
    if not avg_temps:
        return ""
        
    # Сортируем ключи по алфавиту. Функция max() при равенстве значений
    sorted_cities = sorted(avg_temps.keys())
    return max(sorted_cities, key=lambda city: avg_temps[city])
