class FilmStudioManager:
    def __init__(self, workers):
        self.workers = workers

    def __del__(self):
        pass

    def sort_by_experience_increase(self, workers):
        sorted_workers = sorted(workers, key = lambda worker1 : worker1.work_experience, reverse = False)
        return sorted_workers
    
    def sort_by_experience_decrease(self, workers):
        sorted_workers = sorted(workers, key = lambda worker1 : worker1.work_experience, reverse = True)
        return sorted_workers

    
    def sort_by_salary_increase(self, workers):
        sorted_workers = sorted(workers, key = lambda worker1 : worker1.wish_salary, reverse =False)
        return sorted_workers

    def sort_by_salary_decrease(self, workers):
        sorted_workers = sorted(workers, key = lambda worker1 : worker1.wish_salary, reverse = True)
        return sorted_workers

    def find_workers(self, workers, profession):
        professionals = []
        for professional in workers:
            if professional.profession == profession:
                professionals.append(professional)
        return professionals
    
