charset=[s for s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

string='H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_8F7GK99J' # C9GGJ

decrypt=[]

for s in string:
	step=5
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
