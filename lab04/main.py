import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    empty_lines_count = sum(1 for line in lines if not line.strip())
    
    valid_records = read_valid(lines)
    
    parsed_count = len(valid_records)
    
    errors_count = len(lines) - empty_lines_count - parsed_count
    
    avg_temps = average_by_city(valid_records)
    
    warmest = warmest_city(valid_records)
    
    warmest_temp = avg_temps[warmest] if warmest else 0.0
    
    print(parsed_count)
    print(errors_count)
    print(f"{warmest_temp:.1f}")

if __name__ == "__main__":
    main()
