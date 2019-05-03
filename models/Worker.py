class Worker:
    def __init__(self, first_name, last_name, profession, deegre,
                 work_experience, created_documental_films, wish_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.deegre = deegre
        self.work_experience = work_experience
        self.created_documental_films = created_documental_films
        self.wish_salary = wish_salary

    def __del__(self):
        pass

    def __str__(self):
        return ('First name of worker {0}, last name of worker = {1}, profession of worker = {2},'
                + 'degree of worker = {3}, work experience of worker = {4}, created documental '
                + 'films = {5}, wish salary = {6}.').format(self.first_name, self.last_name,
                self.profession, self.deegre, self.work_experience,self.created_documental_films,
                                                            self.wish_salary)
