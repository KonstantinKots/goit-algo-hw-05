from datetime import datetime
from pathlib import Path
import re
#Скрипт для виводу стати логування за різними рівнями
#шлях до файлу - обєкт Паз

#Функція для парсингу логів
def parse_log_line(line: str) -> dict:
    log_dic = {}
    line_log = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$', line)
    if line_log:
        log_dic["date_time"] = datetime.strptime(line_log.group(1), "%Y-%m-%d %H:%M:%S")
        log_dic["level_log"] = line_log.group(2)
        log_dic["text"] = line_log.group(3)
    return log_dic

#Функція для завантаження логів з файлу???
def load_logs(file_path: str) -> list:
    try:
        with open (file_path, 'r', encoding='utf-8')  as file:
            return [line.strip() for line in file if line.strip().parse_log_line()]    
    except FileNotFoundError:
        return [] #список словників

#Функція для фільтрації логів з файлу
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter())


# #Функція для підрахунку логів з файлу
def count_logs_by_level(logs: list) -> dict:

# #Функція для форматування та виводу результатів 
def display_log_counts(counts: dict):

def main():
    file_path = Path('logfile.log')
    parse_log_line()
    print(log_dic)



if __name__ == "__main__":
    main()
