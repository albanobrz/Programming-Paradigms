class Employee:
    def __init__(self, name, age, level='junior'):
        self.__name = name
        self.age = age
        self.level = level
        self.salary = self._compute_salary()

    def get_raise(self, bonus): 
        self.salary += bonus

    def get_name(self):
        return self.__name
    
    def inc_age(self):
        self.age += 1
    
    def get_age(self):
        return self.age 
    
    def get_salary(self):
        return self.salary

    def promote(self):
        if self.level == 'junior':
            self.level = 'senior'
        elif self.level == 'senior':
            self.level = 'CEO'
        self.salary = self._compute_salary()
    
    def _compute_salary(self):
        if self.level == 'junior':
            return 10000
        elif self.level == 'senior':
            return 20000
        elif self.level == 'CEO':
            return 30000
        else:
            print('unknown level')