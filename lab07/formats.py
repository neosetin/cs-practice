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

def parse_settings(lines: list[str]) -> dict:
    res = {}
    last_key = None
    
    for line in lines:
        if '#' in line:
            line = line.split('#', 1)[0]
            
        line = line.strip()
        if not line:
            continue

        if line.startswith('-'):
            item = line[1:].strip()
            if last_key is not None and last_key in res:
                res[last_key].append(item)
            continue

        if ':' in line:
            k, v = line.split(':', 1)
            k = k.strip()
            v = v.strip()
            
            if not v:
                last_key = k
                res[last_key] = []
            else:
                last_key = None
                
                if v.lower() in ('true', 'yes'):
                    v = True
                elif v.lower() in ('false', 'no'):
                    v = False
                else:
                    try:
                        v = int(v)
                    except ValueError:
                        try:
                            v = float(v)
                        except ValueError:
                            pass 
                        
                res[k] = v
                
    return res

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    for row in rows:
        if key in row:
            val = str(row[key])
            if val in extra:
                info = extra[val]
                for k, v in info.items():
                    if k not in row:
                        row[k] = v
    return rows

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
