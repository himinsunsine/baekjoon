n = int(input())
string = []

for i in range(n):
    word = input()
    string.append(word)

string=list(set(string))

string.sort(key=lambda string:(len(string),string))

for i in range(len(string)):
    print(string[i])
