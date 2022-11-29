M = [0 for i in range(12)]

M[0] = "January"
M[1] = "February"
M[2] = "March"
M[3] = "April"
M[4] = "May"
M[5] = "June"
M[6] = "July"
M[7] = "August"
M[8] = "September"
M[9] = "October"
M[10] = "November"
M[11] = "December"

Stone = [0 for i in range(12)]

Stone[0] = 'Garnet'
Stone[1] = 'Amethyst'
Stone[2] = 'Aquamarine'
Stone[3] = "April"
Stone[4] = "Emerald"
Stone[5] = "Pearl"
Stone[6] = "Ruby"
Stone[7] = "Peridot"
Stone[8] = "Sapphire"
Stone[9] = "Opal"
Stone[10] = "Topaz"
Stone[11] = "Tanzanite"

user_input = input("What month were you born?:", )
count = 0

for i in range(len(M)):
    if user_input == M[i]:
        print("Your birthstone for", M[i], "is", Stone[i])
        count += 1
        break