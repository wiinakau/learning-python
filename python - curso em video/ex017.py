from math import pow, hypot
catetoopo = float(input('Digite o valor do cateto oposto: '))
catetoadj = float(input('Digite o valor do cateto adjacente: '))

#hipotenusa = (catetoopo, catetoadj)
hipotenusa = pow(pow(catetoopo, 2) + pow(catetoadj, 2), 1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

