from models.Worker import Worker
from models.Scenario import Scenario

class Director(Worker):
    def __init__(self, first_name, last_name, profession, deegre,
                 work_experience, created_documental_films, wish_salary,
                 Scenario):
        Worker.__init__(self, first_name, last_name, profession, deegre,
                 work_experience, created_documental_films, wish_salary)
        self.Scenario = Scenario

    def __del__(self):
        pass

    def __str__(self):
        return ('First name of worker {0}, last name of worker = {1}, profession of worker = {2},'
                + 'degree of worker = {3}, work experience of worker = {4}, created documental '
                + 'films = {5}, wish salary = {6}, scenarios = {7}.').format(self.first_name, self.last_name,
                self.profession, self.deegre, self.work_experience, self.created_documental_films,
                  self.wish_salary, self.Scenario)

