# Task 1: Calculate weight on Mars
def mars_conversion():
    try:
        user_weight = float(input("Please provide your Earth weight: "))
        weight_on_mars = round(user_weight * 0.378, 2)
        print(f"On Mars, you would weigh: {weight_on_mars}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 2: Calculate weight on any planet in the solar system
def planet_weight_converter():
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    try:
        earth_mass = float(input("Input your weight (Earth): "))
        chosen_planet = input("Name a planet: ").strip().capitalize()
        if chosen_planet in gravity_factors:
            result = round(earth_mass * gravity_factors[chosen_planet], 2)
            print(f"Your weight on {chosen_planet}: {result}")
        else:
            print("Planet not found in the system.")
    except ValueError:
        print("Weight must be a number.")

if __name__ == "__main__":
    mars_conversion()
    planet_weight_converter()