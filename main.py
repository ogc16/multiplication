def generate_multiplication_table(number):
    for i in range():
        result = i * number
        print(f"{i} x {number} = {result}")

number = int(input("Please choose a number: "))
"""generate_multiplication_table(number)"""
score = 0
counter=0
x=int(input("what the minimum number you want to multiply it by?:"))
y=int(input("what the maximum number you want to multiply it by?:"))
y+=1
counter=y-x 
for i in range(x, y):
    result = int(input(f"What is {i} x {number}? "))
    if result == i * number:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
if score ==0.5*counter:
  print("you got",score,"out of",counter,",average.")
elif score >=0.75*counter:
  print("you got",score,"out of",counter,". Keep it up!")
elif score <=0.5*counter:
  print("You scored" ,score,"out of",counter,". Keep practicing!")
