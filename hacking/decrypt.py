with open('message2.txt','r') as file:
        string=file.read()

strlist=[int(x)%41 for x in string.split()]

inverse=[]
step=0

for l in strlist:
        while (l*step)%41 != 1:
                step+=1
        inverse.append(step)
        step=0

decrypt=[]

for l in inverse:
        if l >= 1 and l <= 26:
                decrypt.append(chr(l+64))
        elif l >= 27 and l <= 36:
                decrypt.append(chr(l+21))
        else:
                decrypt.append('_')

print('picoCTF{%s}'%"".join(decrypt))
