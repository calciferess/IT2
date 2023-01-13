#Oppgave 17

random_goated_characters = ["Eren","Mikasa","Mahito","Maki","Aki","Grimmjow","Gatsu","Casca","Yuki","Shion","Shugen","Reigen","Ekubo"]

longest = random_goated_characters[0]
shortest = random_goated_characters[0]

for i in range(len(random_goated_characters)):
    if len((random_goated_characters[i])) > len(longest):
        longest = random_goated_characters[i]
    if len((random_goated_characters[i])) < len(shortest):
        shortest = random_goated_characters[i]

print(longest)
print(shortest)
