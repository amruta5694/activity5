ex2_path = "exercise/ex2.enc"
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

alphabet = "abcdefghijklmnopqrstuvwxyz"

def cipherSubMessage(cipher, message):
    real = ""
    if len(cipher) == len(message):
        for i in range(len(message)):
            real = real + alphabet[(ord(cipher[i])-ord(message[i]))%26]
    return real

with open(ex2_path, 'r') as file:
    data = file.read().replace('\n', '')

for d in data.split(' '):
    for day in days:
        key = cipherSubMessage(d, day)
        if key != "":
            print(key, d, day)

key = "ecms"
starting_point = [0,2,0,3,3,0]
ind = 0
for d in data.split(' '):
    pointer = starting_point[ind]
    k = ""
    for c in d:
        k += key[pointer]
        pointer = (pointer + 1)%4
    print(cipherSubMessage(d, k))
    ind += 1