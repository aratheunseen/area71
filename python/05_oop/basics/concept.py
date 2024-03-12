class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year = 2024):
        return current_year - self.birthyear
    
        
user = User(name="john", birthyear=1999)
print(user.age(current_year = 2023))
print(user.get_name())