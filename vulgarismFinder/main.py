bannedThings = ['duck', 'gross', 'dog', 'nuggets', 'ugly']
counted = 0

print("Type your messages, list or whatever to check for vulgarism :) No letter limits!\n")
check = input("Check your string: ")

for word in bannedThings:
    if check.find(word) != -1:
        counted += 1

if counted != 0:
    print("Found:", counted, "vulgarisms! :(")
else:
    print("Found:", counted, "vulgarisms! :)")