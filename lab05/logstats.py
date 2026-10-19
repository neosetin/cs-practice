def parse_event(line: str) -> dict:
    cleaned_line = line.rstrip('\n')
    
    parts = cleaned_line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректный формат строки лога")
        
    time, level, message = parts
    
    allowed_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in allowed_levels:
        raise ValueError(f"Неизвестный уровень логирования: {level}")
        
    return {"time": time, "level": level, "message": message}
