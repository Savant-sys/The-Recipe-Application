# business layer

# class to get meal categories
class Category:
    def __init__(self, category):
        self.__category = category

    def get_name(self):
        return self.__category

    def set_name(self, category):
        self.__category = category


class Meal:
    def __init__(self, meal_id, meal_name, meal_thumb):
        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_name(self):
        return self.__meal_name

    def set_name(self, meal_name):
        self.__meal_name = meal_name

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


class Area:
    def __init__(self, area):
        self.__area = area
    
    def get_area(self):
        return self.__area


class Instructions:
    def __init__(self, instructions):
        self.__instructions = instructions
    
    def get_instructions(self):
        return self.__instructions


class Ingredient:
    def __init__(self, ingredient, measurement):
        self.__ingredient = ingredient
        self.__measurement = measurement

    def get_ingredient(self):
        return self.__ingredient

    def get_measurement(self):
        return self.__measurement
