#This removes the square brackets and apostrophes from the malicious processes' names
with open('clean.csv', 'r') as clean:
    for line in clean:
        print(line[2:-3])