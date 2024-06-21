
from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Абстрактный родительский класс для взаимодействия с API
    """

    @abstractmethod
    def load_vacancies(self, *args, **kwargs):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {"text": "", "only_with_salary": True, "area": "113", "page": 0, "per_page": 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 1:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1


