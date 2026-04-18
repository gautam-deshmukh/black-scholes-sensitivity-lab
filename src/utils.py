def get_float_input(prompt):
    """
    Safely collect a floating-point input from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
