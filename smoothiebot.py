# --- Define your functions below! ---
start = '''
Welcome to SI Smoothies! 
'''
print(start)

def smoothie_order():
    ingredient = input('Hi there! Do you want a smoothie?')
    if ingredient == 'yes' or ingredient == 'Yes':
        ingredient_2 = input("Awesome! What do you want to start with? We have strawberries, bananas, or kiwi.")
        if ingredient_2 == "banana " or ingredient_2 == "strawberries " or ingredient_2 =='kiwi':
            ingredient_2a = input("For your next ingredient do you want peaches, dragon fruit, blueberries?")
            print("Your " + ingredient_2 + " " + ingredient_2a + " smoothie is ready! Enjoy!")
    elif ingredient != 'yes' or ingredient != 'Yes': 
        print("You're missing out!")
    
print(smoothie_order())






