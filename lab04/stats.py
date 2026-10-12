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
        
    return {"city": city, "temp": temp, "date": date}
