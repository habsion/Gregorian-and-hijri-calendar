import calendar
from hijri_converter import Gregorian
y=int(input('Enter year: '))
m=int(input('Enter month as a number: '))
mon=calendar.month(y,m).split('\n')
print('\n'.join(mon[:2]),'\n','-'*20,sep='')
t=len(mon[2].split())
print(mon[2],'\n',' '*3*(7-t),' '.join(str(Gregorian(y, m, i).to_hijri()).split('-')[2] for i in range(1,t+1)),sep='')
for i in mon[3:]:
    print('-'*20+'\n',i,'\n',' '.join(str(Gregorian(y, m, int(j)).to_hijri()).split('-')[2] for j in i.split()),sep='')
