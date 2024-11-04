class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

# divide 1
    # def divide(self, a, b):
    #     result = 0
    #     while a >= b:
    #         a = self.subtract(a, b)
    #         result += 1
    #     return result

# divide 2
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result


# # mod 1
#     def modulo(self, a, b):
#         while a >= b:
#             a = a-b
#         return a

 # mod 2


    def modulo(self, a, b):
        if b == 0:
            # ขว้าง ZeroDivisionError ถ้า b เป็น 0
            raise ZeroDivisionError("Cannot modulo by zero")
        while a >= b:
            a = a - b
        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
