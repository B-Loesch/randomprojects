import random

numberOfStreaks = 0 #global variable is set to be referenced out of the local scope

for experimentNumber in range(10000):
#Code that creates a list of 100 'heads' or 'tails' values.
    rolls = [] #creates a new list for this set of coin flips, if created outside local scope each loop will append to the original loop
    for i in range(100):
        rolls.append(random.randint(0,1))
# Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1 #all streaks begin at 1, created in local scope so streaks aren't counted between rolls of 100
    for i in range(1, len(rolls)):
        if rolls[i]==rolls[i-1]: #current roll must equal the previous
            streak+=1
        else:
            streak = 1 #resets streak to 1
        if streak == 6:
            numberOfStreaks+=1
            break #once a streak is found it is counted, if not the percentage may go over 100

print('Chance of streak: %s%%' % (numberOfStreaks/100))


        
        
    
