class Calculator:
    def __init__(self):
        print(" Welcome to SpartanCalc CLI Edition ")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y

    def modulus(self, x, y):
        return x % y

    def power(self, x, y):
        return x ** y

    def operate(self, x, op, y):
        if op == '+':
            return self.add(x, y)
        elif op == '-':
            return self.subtract(x, y)
        elif op == '*':
            return self.multiply(x, y)
        elif op == '/':
            return self.divide(x, y)
        elif op == '%':
            return self.modulus(x, y)
        elif op == '**':
            return self.power(x, y)
        else:
            raise ValueError("Invalid operator.")

    def run(self):
        try:
            while True:
                try:
                    x = float(input("Enter first number: "))
                    op = input("Enter operator (+, -, *, /, %, **): ").strip()
                    y = float(input("Enter second number: "))

                    result = self.operate(x, op, y)
                    print(f" Result: {result}")

                except ValueError as ve:
                    print(f" Error: {ve}")
                except ZeroDivisionError as zde:
                    print(f" Error: {zde}")

                cont = input("Do another? (y/n): ").strip().lower()
                if cont != 'y':
                    print(" Thanks for using SpartanCalc!")
                break
        except KeyboardInterrupt:
            print("\n Interrupted. Exiting SpartanCalc. Stay sharp, Spartan!")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()