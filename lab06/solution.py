import os

def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = {}
    for path in paths:
        
        filename = os.path.basename(path)
        
        if "." in filename:
            ext = filename.split(".")[-1].lower()
        else:
            ext = ""

        extensions[ext] = extensions.get(ext, 0) + 1
    return extensions

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
