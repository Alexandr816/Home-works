class Calculator:
   def multiply(self, x, y):
       return x * y

   def division(self, x, y):
       return x / y

   def subtraction(self, x, y):
       return x - y

   def adding(self, x, y):
       return x + y


dp = Calculator
print(dp.multiply(Calculator,2,90))

print(dp.adding(Calculator,2,90))

print(dp.subtraction(Calculator,2,90))

print(dp.division(Calculator,2,90))
