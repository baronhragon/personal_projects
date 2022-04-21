
def diffie(p,g,a,b):
        a_message=(g**a)%p
        b_message=(g**b)%p

        if (b_message**a)%p==(a_message**b)%p:
                return (b_message**a)%p

        else:
                print('a and b dont match')

charset=[s for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

string='H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_8F7GK99J' # C9GGJ

decrypt=[]

for s in string:
	step=diffie(13,5,7,3)
	if s == '_':
		decrypt.append(s)
	else:
		idx=charset.index(s)
		for _ in range(step):
			if idx < 0:
				idx+=len(charset)
			idx-=1
		decrypt.append(charset[idx])


print('picoCTF{%s}'%''.join(decrypt))
