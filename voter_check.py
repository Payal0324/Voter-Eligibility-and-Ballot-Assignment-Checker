# One voter at the polling station
age = 17
is_citizen = True
voter_id = 1001

print("Voter ID:", voter_id)
print("Age:", age)
if age >= 65 and is_citizen:
    print("Eligible")
    print("Senior")
elif age >= 18 and is_citizen:
    print("Eligible")
    print("General")
else:
    print("Not eligible")
    print("Cannot vote")

print("---")

# More voters in line, including a non-citizen
voters = [(17, True), (18, True), (70, True), (30, False)]
for voter_age, voter_is_citizen in voters:
    print("Age:", voter_age)
    if voter_age >= 65 and voter_is_citizen:
        print("Eligible")
        print("Senior")
    elif voter_age >= 18 and voter_is_citizen:
        print("Eligible")
        print("General")
    else:
        print("Not eligible")
        print("Cannot vote")

print("---")

# Countdown to closing time
minutes = 5
while minutes >= 1:
    unit = "minute" if minutes == 1 else "minutes"
    print("Polling station closes in", minutes, unit)
    minutes = minutes - 1
print("Closed")