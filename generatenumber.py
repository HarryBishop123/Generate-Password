import random
computer_score = 0
generate_number = random.randint(8,12)
string = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%^&*()_+-="
symbols = '$%^&*()_-+='
passLen = generate_number
generate_password = "".join(random.sample(string,passLen))
lower = sum([int(c.islower()) for c in generate_password])
if lower > 0:
    computer_score = computer_score + 5
upper = sum([int(c.isupper()) for c in generate_password])
if upper > 0:
    computer_score = computer_score + 5
integer = sum([int(c.isdigit()) for c  in generate_password])
if integer > 0:
    computer_score = computer_score + 5
for c in symbols:
    if c in generate_password:
        computer_score = computer_score + 5
print(generate_password)
print(computer_score)
    
