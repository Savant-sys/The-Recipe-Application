import requests
import textwrap


def show_title():
    print("My Recipe Program")
    print()


def show_menu():
    print("COMMAND MENU")
    print("1 - List all categories")
    print("2 - List all meals for categories")
    print("3 - Search meal by name")
    print("4 - Get a random meal")
    print("5 - List all areas")
    print("6 - List all meals for an area")
    print("7 - Display menu")
    print("0 - Exit the application")
    print()


def list_categories():
    categories = requests.get_categories()

    if categories is None:
        print("\nTechnical difficulties, please try again later")
    else:
        print("\nCATEGORIES")
        for i in range(len(categories)):
            category = categories[i]
            print("  " + category.get_name())
        print()


def list_meals(title, meals):
    if meals is None:
        print("Technical difficulties, please try again later")
    else:
        print(title.upper(), "MEALS")
        for i in range(len(meals)):
            meal = meals[i]
            print("  " + meal.get_name())
        print()


def list_meals_by_category():
    lookup_category = input("Enter a category: ")
    print()
    categories = requests.get_categories()
    found = False

    if categories is None:
        print("Technical difficulties, please try again later")
    else:
        for i in range(len(categories)):
            category = categories[i]
            if category.get_name().lower() == lookup_category.lower():
                found = True
                break
        if found:
            meals = requests.get_meal_by_category(lookup_category)
            list_meals(lookup_category, meals)

        else:
            print("Invalid category, please try again")


def list_areas():
    areas = requests.get_areas()

    if areas is not None:
        print()
        print("AREAS")
        for i in range(len(areas)):
            area = areas[i]
            print("  " + area.get_area())
        print()
    else:
        print("\nTechnical difficulties, please try again later\n")


def list_meals_by_area():
    lookup_area = input("Enter an area: ")

    areas = requests.get_areas()
    
    if areas is not None:
        found = False
        for i in range(len(areas)):
            area = areas[i]
            if area.get_area().lower() == lookup_area.lower():
                found = True
                break

        if found:
            meals = requests.get_meal_by_area(lookup_area)
            print()

            if meals is not None:
                # if the category is found then all the meals for the
                # category that was searched gets printed
                print("MEALS FOR " + lookup_area.upper())
                for i in range(len(meals)):
                    meal = meals[i]
                    print("  " + meal.get_name())
                print()
            else:
                print("Technical difficulties, please try again later\n")
        else:
            print("Invalid area. Please try again")
    else:
        print("\nTechnical difficulties, please try again later\n")


def format_instruction(first_letter, index):
    instructions = requests.get_meal_instructions(first_letter)

    if instructions is not None:
        meal_instructions = instructions[index]
        my_wrap = textwrap.TextWrapper(width=80)
        wrap_list = my_wrap.wrap(text=meal_instructions.get_instructions())
    else:
        print("\nTechnical difficulties, please try again later\n")

    return wrap_list


def list_ingredients(name):
    ingredients = requests.get_ingredients(name) 

    if ingredients is not None:
        for i in range(len(ingredients)):
            ingredient = ingredients[i]
            print("{:17} {:<10}".format(ingredient.get_measurement(), ingredient.get_ingredient()))
    else:
        print("\nTechnical difficulties, please try again later\n")


# prompts user to search for a meal to display its recipe with instructions and ingredients
def search_meals():
    name = input("SEARCH FOR MEAL: ")
    first_letter = name[0]

    meals = requests.get_all_meals(first_letter)

    if meals is not None:
        found = False 

        for i in range(len(meals)):
            meal = meals[i]
            if meal.get_name().lower() == name.lower():
                found = True
                index = i
                break
        if found:
            print("\nRecipe: " + meal.get_name())
            print("\nInstructions:\n" + format_instruction(first_letter, index))
            print("\nIngredients:")
            print("{:17} {:<10}".format("Measure", "Ingredient"))
            print("-"*80)
            list_ingredients(name)
        else:
            print("Invalid meal")

        print()
    else:
        print("\nTechnical difficulties, please try again later\n")


# Returns the name of a random meal
def get_random_meal_name():
    meal = requests.get_random_meal()

    if meal is not None:
        print("A random meal was selected just for you!")
        random_meal = meal[0]
    else:
        print("\nTechnical difficulties, please try again later\n")

    return random_meal.get_name()


# takes the random meal name and displays its recipe with instructions and ingredients
def random_meal():
    random_meal = get_random_meal_name()
    first_letter = random_meal[0]
    meals = requests.get_all_meals(first_letter)

    if meals is not None:
        found = False 
        for i in range(len(meals)):
            meal = meals[i]
            if meal.get_name().lower() == random_meal.lower():
                found = True
                index = i
                break
        if found:
            print("\nRecipe: " + random_meal )
            print("\nInstructions:\n" + format_instruction(first_letter, index))
            print("\nIngredients:")
            print("{:17} {:<10}".format("Measure", "Ingredient"))
            print("-"*80)
            list_ingredients(random_meal)
            print()
        else:
            print("No meal found")
    else:
        print("\nTechnical difficulties, please try again later\n")


def main():
    show_title()
    show_menu()

    # Loops the choices for the menu options
    while True:
        command = input("What would you like to do?: ")
        if command == "1":
            list_categories()
        elif command == "2":
            list_meals_by_category()
        elif command == "3":
            search_meals()
        elif command == "4":
            random_meal()
        elif command == "5":
            list_areas()
        elif command == "6":
            list_meals_by_area()
        elif command == "7":
            print()
            show_menu()
        elif command == "0":
            print("Thank you for dining with us!")
            break
        else:
            print("Please enter a valid choice on the menu 0-7\n")
            continue


if __name__ == "__main__":
    main()

