# Day 1: Study Time Calculator

name = input("What is your name? ").strip()
reason = input("What are you learning Python for? ").strip()
minutes = int(input("How many minutes did you study yesterday? "))
minutes = int(input("How many minutes did you study today? "))

hours = minutes / 60

print("\n--- Study Summary ---")
print(f"Hello {name}!, your learning goal is: {reason}.")
print(f"That is {hours:.1f} hours of learning.")
print("Keep up the good work!")

