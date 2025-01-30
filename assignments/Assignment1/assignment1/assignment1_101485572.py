# Author: Breno Lopes Mafra (101485572)
# Assignment: #1

gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5   # Float
highest_reps = 25            # Integer
membership_active = True     # Boolean

# Dictionary where keys are people names (strings) and values are 
# tuples of three integers representing workout minutes for
# Yoga, Running, Weightlifting
workout_stats = {"Breno":(30, 45, 20), 
                 "Pedro":(40, 50, 30), 
                 "Nazyrha":(50, 60, 40),
                 "Alex":(60, 70, 50),
                 "Ethan":(70, 80, 60)}

for i in list(workout_stats.keys()):
    sumOfMinutes = sum(workout_stats[i])
    workout_stats[i + "_Total"] = sumOfMinutes

# Nested list to store workout minutes per activity for each person
workout_list = []
for personName in workout_stats.keys():
    if "_Total" not in personName:
        activities = list(workout_stats[personName])
        workout_list.append(activities)

# Total minutes for each activity for each person
print("")
print("Total minutes for Yoga and Running for all people:")
for personMinutes in workout_list:
    print(personMinutes[0:2]) 

# Total minutes for each person
print("")
print("Total Weightlifting minutes for the last two people:")
for personMinutes in workout_list[-2:]:
    print(personMinutes[2])

# Message to people with more than 120 minutes total
for person in workout_stats:
    if "_Total" in person and workout_stats[person] >= 120:
        print("")
        print("Great job staying active, " + person.replace('_Total', '') + "!")

# Input loop for checking a people's details
while True:
    try:
        print("")
        person_name = input("Enter a people's name to check their workout details: ").capitalize()
        if person_name in workout_stats and "_Total" not in person_name:
            activities = workout_stats[person_name]
            total_minutes = workout_stats[person_name + "_Total"]
            print("")
            print("Workout minutes for Yoga: " + str(activities[0]) + 
                ", Running: " + str(activities[1]) + 
                ", Weightlifting: " + str(activities[2]))
            print("")
            print (person_name + "'s total workout minutes: " + 
                str(total_minutes))
            break
        else:
            raise ValueError("Person not found.")
    except ValueError as e:
        print(e)

# Find the person with the highest and lowest total workout minutes
max_total = -1
min_total = float('inf')
max_person = ""
min_person = ""

for person in workout_stats:
    if "_Total" in person:
        if workout_stats[person] > -1:
            max_total = workout_stats[person]
            max_person = person.replace('_Total', '')
        if workout_stats[person] < min_total:
            min_total = workout_stats[person]
            min_person = person.replace('_Total', '')

print("")
print(max_person + " has the highest total workout minutes: " + str(max_total) + " minutes")
print("")
print(min_person + " has the lowest total workout minutes: " + str(min_total) + " minutes")
