import os

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        
        filename = path.split("/")[-1]

        if "." in filename and not filename.startswith("."):
            ext = filename.split(".")[-1].lower()
        else:
            ext = ""

        if ext in result:
            result[ext] += 1
        else:
            result[ext] = 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    return min(paths, key=lambda p: (-p.count("/"), p))

def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"

    units = ["КБ", "МБ", "ГБ", "ТБ"]
    value = n_bytes / 1024
    unit_index = 0

    while value >= 1024 and unit_index < len(units) - 1:
        value /= 1024
        unit_index += 1

    return f"{value:.1f} {units[unit_index]}"
