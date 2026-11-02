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
            parts_comment = line.split('#', 1)
            line = parts_comment[0]
            
        line = line.strip()
        if not line:
            continue

        if line.startswith('-'):
            item = line[1:].strip()
            if last_key in res:
                res[last_key].append(item)
            continue

        if ':' in line:
            parts = line.split(':', 1)
            k = parts[0].strip()
            v = parts[1].strip()
            
            if not v:
                last_key = k
                res[last_key] = []
            else:
                if v.isdigit():
                    v = int(v)
                elif '.' in v and v.replace('.', '', 1).isdigit():
                    v = float(v)
                elif v in ['true', 'yes']:
                    v = True
                elif v in ['false', 'no']:
                    v = False
                    
                res[k] = v
                last_key = None
                
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
