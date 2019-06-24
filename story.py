start = '''
Your friend has just moved to sunny California and she doesn/t know where she is. Your task is to find her before she gets even more lost. 
''' 
keepplaying = "yes"
print(start)

while keepplaying == "Yes" or keepplaying == "yes":
    userchoice = input("Should I go left or right?")
    if userchoice == "left" or userchoice == "Left":
        print('You found your friend! ')
        print("")
        keepplaying = input("Would you like to try again? Type yes or no.")
    if keepplaying == "no":
        quit()
    else: 
        print(start)
    elif userchoice == "right" or userchoice == "Right":
        print("Your friend is no where to be seen. She will be lost forever.")
        keepplaying = input('Would you like to try again? Type yes or no.')
    if keepplaying == "no":
        quit()
    else:
        print("Not a valid answer. Try again.")
        keepplaying = input('Would you like to try again? Type yes or no.')
    if keepplaying == "no":
        quit()
keepplaying = "yes"
while keepplaying == "yes" or keepplaying == "Yes":
    print(start)

