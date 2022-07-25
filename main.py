from playsound import playsound

file = open("song.txt", "r")

tmp_line = line = ""
while (1):
    tmp_line = file.readline()
    if (not tmp_line):
        break
    print(tmp_line.strip())
    line += tmp_line

l = line.split()

#l = [line.rstrip() for line in l]
#print(line.split(), "\n\n", l)

print(l)

i = 0
for i in range(len(l)):
    if (l[i] == 'AM' or 'Am' or 'aM' or 'am') :
        playsound(l[i]+".mp3", True)
        print("\n I am playing chord ", l[i] + ".mp3\n")
    elif (l[i] == 'DM' or 'Dm' or 'dM' or 'dm') :
        playsound(l[i]+".mp3", True)
        print("\n I am playing chord ", l[i] + ".mp3\n")
    elif (l[i] == 'C' or 'c') :
        playsound('C.mp3', True)
        print("\n I am playing chord ", l[i] + ".mp3\n")
    elif (l[i] == 'G' or 'g') :
        playsound('G.mp3', True)
        print("\n I am playing chord ", l[i] + ".mp3\n")
    elif (l[i] == 'E' or 'e') :
        playsound('E.mp3', True)
        print("\n I am playing chord ", l[i] + ".mp3\n")
    else:
        pass
    print("  Sucsess = ", l[i])
    i += 1

file.close()





