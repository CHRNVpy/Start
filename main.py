import json
import re
from datetime import datetime


with open('results_RUN.txt', 'r', encoding='utf-8-sig') as f:
    content = f.readlines()
# print(content)

with open('competitors2.json', 'r', encoding='utf-8') as j:
    competitors = json.load(j)

results = []
for key, value in competitors.items():
    matching_entities = [entity.strip() for entity in content if entity.strip().startswith(f'{key} ')]
    if matching_entities:
        start = re.search(r'\d{2}:\d{2}:\d{2},\d{6}', matching_entities[0]).group()
        finish = re.search(r'\d{2}:\d{2}:\d{2},\d{6}', matching_entities[1]).group()
        start_time = datetime.strptime(start, '%H:%M:%S,%f')
        finish_time = datetime.strptime(finish, '%H:%M:%S,%f')
        result = finish_time - start_time
        seconds = result.total_seconds()
        minutes, seconds = divmod(seconds, 60)
        formatted_result = "{:02d}:{:05.2f}".format(int(minutes), seconds).replace('.', ',')
        results.append(f'{key} {value["Surname"]} {value["Name"]} {formatted_result}')

def get_time(entry):
    time_str = entry.split()[3]
    return time_str

sorted_data = sorted(results, key=get_time)
print(f'Занятое место | Нагрудный номер | Имя | Фамилия | Результат')
for i, entry in enumerate(sorted_data, start=1):
    print(i, entry)
