totalVowelsinStr = 0
vowels =['a','e','i','o','u']
for x in vowels:
    totalVowelsinStr = totalVowelsinStr + s.count(x)
print("Number of vowels: " + str(totalVowelsinStr))
