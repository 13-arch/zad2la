input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
prost=[1,3,5,7,11,13,17,19,23]
a=int(data)
if a in prost :
    output_data.write('Y')
else :
    output_data.write('N')    
output_data.close()
input_data.close()

#2 способ
input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()

data = data.split()

a = int(data[0])

for i in range(2, 26):
    if a%i == 0 and i != a:
        output.write(str('N'))
        break
    elif i == a:
        output.write(str('Y'))

if a == 1:
    output.write(str('N'))      

input_data.close()
output.close()