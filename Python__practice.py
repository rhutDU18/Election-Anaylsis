counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
    if counties[3] != 'Jefferson':
        print(counties[2])

temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on AC.")
else:
    print("Open the windows.")

#What is the score
score = int(input("What is the test score"))

#Determine the grade 
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your score is a B.')
    else:
        if score >= 70:
             print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# What is the score?
score = int(input("Whaat is your test score?"))

#Deter,ine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D')
else:
    print('Your grade is an F')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("EL Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties")

