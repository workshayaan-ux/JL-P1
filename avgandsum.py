numbers = []

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)

    print("Total sum:", total)
    print("Average:", average)
else:
    print("No numbers were entered.")