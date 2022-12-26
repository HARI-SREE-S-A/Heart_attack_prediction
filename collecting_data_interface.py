data = (1,1,1,1,1,1,1,1,1,1,1,1,1)
a = int(input('age '))
b = int(input('sex '))
c = int(input('Chest pain type '))
d = int(input('BP '))
e = int(input('Cholesterol '))
f = int(input('FBS over 120 '))
g = int(input('EKG results '))
h = int(input('Max HR '))
j = int(input('Exercise angina '))
k = float(input('ST depression ')) 
l = int(input('Slope of ST '))
m = int(input('Number of vessels fluro '))
n = int(input('Thallium '))
li = [a,b,c,d,e,f,g,h,j,k,l,m,n]
data_list  = np.asarray(data)
for i in range(len(data)):
    data_list[i] = li[i]
#print(data_list)
data_list = np.asarray(data)
reshaped = data_list.reshape(1,-1)

prediction = model.predict(reshaped)

if prediction == 'Presence':
    print('Prone to heart attack')
else:
    print('your heart is safe')
