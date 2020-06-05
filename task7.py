class ComplexNumbers:
    def __init__(self, first_num, second_num):
        self.number1 = float(first_num)
        self.number2 = float(second_num.replace('j', '').replace('i', ''))

    @classmethod
    def check(cls, obj1, obj2):
        """Check result of sum and multiplication by inbuilt python methods"""
        print('Checking result:')
        return f'Result of sum is: {complex(obj1.number1, obj1.number2) + complex(obj2.number1, obj2.number2)}\n\
Result of multiplication is {complex(obj1.number1, obj1.number2) * complex(obj2.number1, obj2.number2)}'

    def __add__(self, other):
        return f'Result of sum of two complex num is:  {self.number1 + other.number1}\
{"+" if (self.number2 + other.number2) >= 0 else ""}{self.number2 + other.number2}j'

    def __mul__(self, other):
        return f'Result of multiplication of two complex num is:  \
{(self.number1 * other.number1 - self.number2 * other.number2)}{"+" if (self.number2 + other.number2) >= 0 else ""}\
{(self.number1 * other.number2 + other.number1 * self.number2)}j '


try:
    print('Complex number is an expression of the form "a + bj\nYour first complex number:')
    first_complex = ComplexNumbers(input('Enter first part, a = '), input('Enter seсond part, bj = '))
    print('Your second complex number:')
    second_complex = ComplexNumbers(input('Enter first part, a = '), input('Enter seсond part, bj = '))
    print(first_complex + second_complex)
    print(first_complex * second_complex)
    print(ComplexNumbers.check(first_complex, second_complex))
except ValueError as v:
    print(f'You enter wrong number: {v}')
