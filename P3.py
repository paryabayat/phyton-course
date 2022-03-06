print("EXERCISE 1:")
income = input('please insert your monthly income here (Between 0 to 6k or more then 8k per month): ')
income = int(income)
if income <= 1000:
    result = income
if income > 1000 and income <= 2500:
    result = income - (income * 0.10)
if income > 2500 and income <= 4000:
    result = income - (income * 0.15)
if income > 4000 and income <= 6000:
    result = income - (income * 0.20)
if income > 8000:
    result = income - (income * 0.30)
print(result)

print("EXERCISE 2:")
sideA = input("Please insert side A : ")
sideB = input("Please insert side B : ")
sideC = input("Please insert side C : ")
sideA = int(sideA)
sideB = int(sideB)
sideC = int(sideC)
situation1 = sideA*2 + sideB*2
situation2 = sideA*2 + sideC*2
situation3 = sideB*2 + sideC*2
if situation1 == sideC*2 or situation2 == sideB or situation3 == sideA:
    print("NOT RIGHT")
else:print("RIGHT triangle")

print("EXERCISE 3:")
NumA = input("please inter the first number : ")
NumB = input("please inter the second number : ")
NumC = input("please inter the third number : ")
NumD = input("please inter the fourth number : ")
NumE = input("please inter the fifth number : ")
NumA = int(NumA)
NumB = int(NumB)
NumC = int(NumC)
NumD = int(NumD)
NumE = int(NumE)
if NumA == NumB or NumA == NumC  or NumA== NumD or NumA == NumE:
    print("DUPLICATES")
elif NumB == NumC or NumB == NumD  or NumB== NumE:
    print("DUPLICATES")
elif NumC == NumD or NumC == NumE:
    print("DUPLICATES")
elif NumE == NumE:
    print("DUPLICATES")
else:print("ALL UNIQUE")