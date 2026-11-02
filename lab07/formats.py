import json

def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []

    all_lines = text.split('\n')
    lines = []
    for line in all_lines:
        line = line.strip()
        if line:
            lines.append(line)
            
    if not lines:
        return []

    headers = []
    for word in lines[0].split(','):
        headers.append(word.strip())
        
    res = []

    for line in lines[1:]:
        vals = []
        for word in line.split(','):
            vals.append(word.strip())
            
        d = {}
        for i in range(len(headers)):
            if i < len(vals):
                d[headers[i]] = vals[i]
            else:
                d[headers[i]] = ""
        res.append(d)
        
    return res
