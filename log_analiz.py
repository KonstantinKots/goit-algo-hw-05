from datetime import datetime
from pathlib import Path
from collections import Counter
import re
import sys
# Скрипт для виводу стати логування за різними рівнями

# Функція для парсингу логів
def parse_log_line(line: str) -> dict:
    log_dic = {}
    line_log = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$', line)
    if line_log:
        log_dic["date_time"] = datetime.strptime(line_log.group(1), "%Y-%m-%d %H:%M:%S")
        log_dic["level"] = line_log.group(2)
        log_dic["text"] = line_log.group(3)
    return log_dic

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    try:
        with open (file_path, 'r', encoding='utf-8')  as file:
            return [parse_log_line(line.strip()) for line in file if line.strip()]    
    except FileNotFoundError:
        return []

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log.get('level') == level]

# Функція для підрахунку записів логів
def count_logs_by_level(logs: list) -> dict:
    counts = Counter(log['level'] for log in logs).most_common()
    return counts

# Функція для форматування та виводу результатів 
def display_log_counts(counts: dict):
    print(f"\n{'Рівень логування':<18} | {'Кількість'}")
    print('-' * 45)
    for level, count in counts:
        print(f"{level:<18} | {count}")

def main():
    try:
        if len(sys.argv) > 1:
            file_path = Path(sys.argv[1])
            logs = load_logs(file_path)
            counts = count_logs_by_level(logs)
            display_log_counts(counts)

            if len(sys.argv) > 2:
                level = sys.argv[2]
                filter_logs = filter_logs_by_level(logs, level)

            print(f"\nДеталі логів для рівня {level}: ")
            if filter_logs:
                for log in filter_logs:
                    print(f"{log['date_time']} - {log['text']}")
            else:
                print("No logs for this level")
        else:
            print("Use: name_script.py <log_file> [level]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
