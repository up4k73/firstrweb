car = 'subaru'
print("Is car == 'subaru'? I predict True")

banned_users = ['igor','masha','vladimir']
user = 'marie'
if user not in banned_users:
    print(user.upper()+" пиш")

aliencolor = 'black'
if 'green' in aliencolor:
    print("wrong color")
elif 'black' in aliencolor:
        print("google")


age = 35
if age < 5:
    print("you suck")
elif age < 20:
    print("fuck")
elif age < 45:
    print("motherfucker")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("adding "+ requested_topping + " .")
    print("\nFinished making yout pizza!")
else:
    print("Are you shure you want a plain pizza?")