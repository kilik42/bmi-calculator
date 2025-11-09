# BMI Calculator (U.S. Units to Metric)

# Ask for user input
weight_lb = float(input("Enter your weight in pounds (lbs): "))
feet = int(input("Enter your height - feet: "))
inches = int(input("Enter your height - inches: "))

# Convert to metric units
weight_kg = weight_lb * 0.45359237
height_m = (feet * 12 + inches) * 0.0254

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Determine BMI category
if bmi < 15:
    category = "Very severely underweight"
elif bmi < 16:
    category = "Severely underweight"
elif bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal (healthy weight)"
elif bmi < 30:
    category = "Overweight"
elif bmi < 35:
    category = "Obese Class I (Moderately obese)"
elif bmi < 40:
    category = "Obese Class II (Severely obese)"
elif bmi < 45:
    category = "Obese Class III (Very severely obese)"
elif bmi < 50:
    category = "Obese Class IV (Morbidly Obese)"
elif bmi < 60:
    category = "Obese Class V (Super Obese)"
else:
    category = "Obese Class VI (Hyper Obese)"

# Calculate BMI Prime (your BMI divided by 25)
bmi_prime = bmi / 25

# Display results
print("\n--- Results ---")
print(f"Your weight in kilograms: {weight_kg:.2f} kg")
print(f"Your height in meters: {height_m:.2f} m")
print(f"Your BMI: {bmi:.2f}")
print(f"BMI Prime: {bmi_prime:.2f}")
print(f"Category: {category}")
