def calculate_bmi(weight, height):
    height_m = float(height) / 100  # Convert height from cm to m
    bmi = float(weight) / (height_m ** 2)
    return bmi

def calculate_calorie_requirements(age, gender, weight, height, activity_level, objective):
    # Calculate BMR (Basal Metabolic Rate) using the Harris-Benedict equation
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * float(age))
    else:
        bmr = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * float(age))

    # Adjust BMR based on activity level
    activity_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    activity_factor = activity_factors.get(activity_level.lower(), 1)
    calorie_intake = bmr * activity_factor
    
    print(calorie_intake)

    if objective == 'gain weight faster':
        calorie_intake += 1000  # Increase calorie intake by 1000 calories for faster weight gain
    elif objective == 'gain weight medium rate':
        calorie_intake += 500  # Increase calorie intake by 500 calories for moderate weight gain
    elif objective == 'gain weight slowly':
        calorie_intake += 250  # Increase calorie intake by 250 calories for slow weight gain
    elif objective == 'lose weight faster':
        calorie_intake -= 1000  # Decrease calorie intake by 1000 calories for faster weight loss
    elif objective == 'lose weight medium rate':
        calorie_intake -= 500  # Decrease calorie intake by 500 calories for moderate weight loss
    elif objective == 'lose weight slowly':
        calorie_intake -= 250  # Decrease calorie intake by 250 calories for slow weight loss


    return calorie_intake

def divide_calories(total_calories):
    breakfast_ratio = 0.225
    lunch_ratio = 0.275
    dinner_ratio = 0.25
    snack_ratio = 0.125

    breakfast_calories = float(total_calories * breakfast_ratio)
    lunch_calories = float(total_calories * lunch_ratio)
    dinner_calories = float(total_calories * dinner_ratio)
    snack_calories = float(total_calories * snack_ratio)

    return [breakfast_calories, snack_calories, lunch_calories, snack_calories, dinner_calories]

def calculate_min_limits(age, weight, gender):
    min_limits = {
    'FatContent': None,
    'SaturatedFatContent': None,
    'CholesterolContent': None,
    'SodiumContent': None,
    'CarbohydrateContent': None,
    'FiberContent': None,
    'SugarContent': None,
    'ProteinContent': None
    }
    weight=float(weight)
    age=float(age)
    if gender.lower() == 'male':
        min_limits['FatContent'] = 15 + (weight / 2)  # Adjust based on weight
        min_limits['SaturatedFatContent'] = 7
        min_limits['CholesterolContent'] = 0
        min_limits['SodiumContent'] = 1500
        min_limits['CarbohydrateContent'] = 130  # No specific minimum limit
        min_limits['FiberContent'] = 30
        min_limits['SugarContent'] = 0  # No specific minimum limit
        min_limits['ProteinContent'] = 56 + (weight / 2)  # Adjust based on weight
    else:
        min_limits['FatContent'] = 12 + (weight / 2)  # Adjust based on weight
        min_limits['SaturatedFatContent'] = 5
        min_limits['CholesterolContent'] = 0
        min_limits['SodiumContent'] = 1500
        min_limits['CarbohydrateContent'] = 130  # No specific minimum limit
        min_limits['FiberContent'] = 25
        min_limits['SugarContent'] = 0  # No specific minimum limit
        min_limits['ProteinContent'] = 46 + (weight / 2)  # Adjust based on weight

    # Adjust min limits based on age if needed
    if age > 50:
        min_limits['SodiumContent'] = 1300  # Increase sodium limit for individuals over 50

    return min_limits

def calculate_max_limits(age, weight, gender):
    max_limits = {
        'FatContent': None,
        'SaturatedFatContent': None,
        'CholesterolContent': None,
        'SodiumContent': None,
        'CarbohydrateContent': None,
        'FiberContent': None,
        'SugarContent': None,
        'ProteinContent': None
    }
    weight=float(weight)
    age=float(age)

    # Set max limits based on gender
    if gender.lower() == 'male':
        max_limits['FatContent'] = 70 + (weight / 2)  # Adjust based on weight
        max_limits['SaturatedFatContent'] = 22
        max_limits['CholesterolContent'] = 300
        max_limits['SodiumContent'] = 2300
        max_limits['CarbohydrateContent'] = 600  # No specific maximum limit
        max_limits['FiberContent'] = 38
        max_limits['SugarContent'] = 36
        max_limits['ProteinContent'] = 56 + (weight / 2)  # Adjust based on weight
    else:
        max_limits['FatContent'] = 55 + (weight / 2)  # Adjust based on weight
        max_limits['SaturatedFatContent'] = 16
        max_limits['CholesterolContent'] = 300
        max_limits['SodiumContent'] = 2300
        max_limits['CarbohydrateContent'] = 600  # No specific maximum limit
        max_limits['FiberContent'] = 25
        max_limits['SugarContent'] = 25
        max_limits['ProteinContent'] = 46 + (weight / 2)  # Adjust based on weight

    # Adjust max limits based on age if needed
    if age > 50:
        max_limits['SodiumContent'] = 1500  # Reduce sodium limit for individuals over 50

    return max_limits

# Example usage

def calculate_average_limits(max_limits, min_limits):
    average_limits = {
    'FatContent': None,
    'SaturatedFatContent': None,
    'CholesterolContent': None,
    'SodiumContent': None,
    'CarbohydrateContent': None,
    'FiberContent': None,
    'SugarContent': None,
    'ProteinContent': None
    }
    for nutrient in average_limits:
        average_limits[nutrient] = (max_limits[nutrient] + min_limits[nutrient]) / 2

    return average_limits

    


