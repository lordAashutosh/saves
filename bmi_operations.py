# < 16.0        Severely Underweight
# 16.0 - 18.4        Underweight
# 18.5 - 24.9        Normal
# 25.0 - 29.9        Overweight
# 30.0 - 34.9        Moderately Obese
# 35.0 - 39.9        Severely Obese
# > 40.0        Morbidly Obese


def bmi_to_remarks(bmi):
    if bmi < 16.0:
        return "Severely Underweight"
    elif 16.0 <= bmi <= 18.4:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    elif 30.0 <= bmi <= 34.9:
        return "Moderately Obese"
    elif 35.0 <= bmi <= 39.9:
        return "Severely Obese"
    else:
        return "Morbidly Obese"


def calculate_bmi(height, weight):
    height_in_square_meter = (float(height) * 0.0254)**2
    bmi = weight/height_in_square_meter
    return round(bmi, 2)