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

