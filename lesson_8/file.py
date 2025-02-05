import requests
from faker import Faker

fake = Faker()

url = " "
t_title = fake.text(max_nb_chars=50)

class SkyToDo:
    def __init__(self, url):
        self.url = url

#   Рандомная таска
    def random_task(self):
        new_t = {
            "title" : t_title,
            "completed" : False
        }
        return new_t
    
# - Создание.
    def create_task(self):
        new_t = self.random_task()
        response = requests.post(self.url, json = new_t)
        return response, new_t

# - Переименование
    def chang_title(self, task_url):
        new_title = { "title" : t_title }
        return requests.patch(f'{self.url}{task_url}', json = new_title)

# - Удаление.
    def delete_task(self, task_url):
        return requests.delete(f'{self.url}{task_url}')

# - Получение списка.
    def get_list(self):
        return requests.get(self.url)
    
# - Получение конкретной задачи из списка.
    def get_task(self, number):
        task_list = self.get_list().json()
        one_task = task_list[number]
        return one_task

# - Снятие / Отметка задачи «Выполнена».
    def task_done(self, task_url, donable=None):
        isCompite = {"completed": donable}
        return requests.patch(f'{self.url}{task_url}', json = isCompite)

# Очистить список
    def terminate_list(self):
        task_list = self.get_list().json()
        for i in range(0, len(task_list)):
            url_t = task_list[i]["url"]
            self.delete_task(url_t)