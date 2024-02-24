# bounce.py
#
# Exercise 1.5

height = 100
for bounce in range(10):
    height = height * 3 / 5
    print(f"Bounce {bounce + 1}: {round(height, 4)}")
