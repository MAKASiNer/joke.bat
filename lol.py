base = "for /L %%{0} in (1, 1, {2}) do mkdir %cd%{1}"
add = ""

header = "@echo off\nmkdir c:\_0\hello\ncd c:\_0\hello\n\n"
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
number = 100

result = list()

for a in alf:
	add += "\%%" + a
	result.append(base.format(a, add, number))

result = header + ' & (\n'.join(result) + "\n)" * (len(alf) - 1) 

file = open("joke.bat", "w")
file.write(result)
file.close()

print(result)
input()