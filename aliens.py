#python dictionaires
# mtb 4.24.2018
alien_0={'color' : 'green','points': 5}
alien_1={'color' : 'yellow','points': 10}
alien_2={'color' : 'red','points': 15}

aliens =[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Make an empty list for storing aliens
aliens_1 = [] 

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green','points': 5, 'speed' : 'slow'}
    aliens_1.append(new_alien)
    
# Show the first 5 aliens
for alien in aliens_1[:5]:
    print(alien)
print("...")

# show how many aliens have been created 
print("Total number of aliens: " + str(len(aliens_1)))
