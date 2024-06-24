import json
from pathlib import Path

# создаем переменные с путями к нужным файлам для импорта:
PARENT_PATH = Path(__file__).parent.parent
DATA_PATH = Path(PARENT_PATH, "data")
VACANCIES_PATH = Path.joinpath(DATA_PATH, 'vacancies.json')

print(VACANCIES_PATH)
print(type(VACANCIES_PATH))



