from logstats import count_levels, top_errors, format_report

def main():
    file_path = input().strip()

    with open(file_path, "r", encoding="utf-8") as log:
        counts = count_levels(log)
    with open(file_path, "r", encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total_lines = sum(counts.values())

    print(total_lines)
    print(counts["ERROR"])
    print(counts["BROKEN"])

    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()
