from managers.FilmStudioManager import FilmStudioManager
from models.Worker import Worker
from models.Director import Director
from models.Actor import Actor
from models.Operator import Operator
from models.Decorator import Decorator
from models.Costumer import Costumer
from models.Roles import Roles
from models.Scenario import Scenario
from models.Clothes import Clothes
from models.Style import Style

director = Director("Anna", "Cinema", "Director", True, 5, 2, 50000, Scenario.INSOMNIA)
operator = Operator("Andrew", "Coala", "Operator", False, 10, 3, 45000, True)
actor = Actor("Evelin", "Holla", "Actor", True, 12, 1, 70000, Roles.DETECTIVE)
decorator = Decorator("Jack", "Smith", "Decorator", False, 4, 0, 30000, True, True)
costumer = Costumer("Mary", "Parker", "Costumer", True, 15, 7, 35000, Clothes.DRESS, Style.CASUAL)
employee_list = [director, operator, actor, decorator, costumer]
print(employee_list)
main_manager = FilmStudioManager(employee_list)
print(main_manager.sort_by_experience_increase(employee_list))
print(main_manager.sort_by_salary_decrease(employee_list))
print(main_manager.find_workers(employee_list, 'Actor'))
