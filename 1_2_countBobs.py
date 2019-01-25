bobs = 0
for i in range (0,len(s)):
    if s[i]=="b":
        if s[i+1]=="o":
            if s[i+2]=="b":
                bobs +=1
    i += 1
print("Number of times bob occurs is: " + str())


#not working. Doesn't count bobob as two bobs.....
