"""My first program."""

print("Hello, my name is Python! Please type your name to continue our conversation.")
name = input()
print(f"Hello {name}! Have you programmed before?")
answer = input()
if answer == "Yes":
    print(f"Congratulations, {name}! It will be a little bit easier for you.")
elif answer == "No":
    print(f"Don`t worry, {name}! You will learn everything you need.")
else:
    print("Your input is incorrect!")
