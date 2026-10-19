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
def count_levels(lines) -> dict:

    counts = {"BROKEN": 0, "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0} 
    for line in lines:
        if not line.strip():
            continue  
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
            
    return counts
