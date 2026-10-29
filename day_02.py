name = input("What is your name? ").strip() .title()
language = input("What language are you learning? ").strip() .title()
goal = input("What is your learning goal? ").strip() .title()
minutes = int(input("How many minutes will you study today? "))

hours = minutes / 60

print("\n--- MY LEARNING PROFILE ---")
print(f"Name: {name}")
print(f"Language: {language}")
print(f"Goal: {goal}")
print(f"Study Time: {minutes} minutes ({hours:.1f} hours)")