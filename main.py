import calendar
from hijri_converter import Gregorian


def hijri_month_name(a):
    return (month_dict[int(str(Gregorian(y, m, 1).to_hijri()).split('-')[1])]+' - '+month_dict[int(str(Gregorian(y, m, a).to_hijri()).split('-')[1])]).center(20)


month_dict = {1: 'محرم', 2: 'صفر', 3: 'ربيع الأول', 4: 'ربيع الثاني', 5: 'جمادي الأولى', 6: 'جمادي الآخرة', 7: 'رجب'
, 8: 'شعبان', 9: 'رمضان', 10: 'شوال', 11: 'ذو القعدة', 12: 'ذو الحجة'}

y=int(input('Enter year: '))
m=int(input('Enter month as a number: '))
mon=calendar.month(y,m).split('\n')
print(mon[0])
print(hijri_month_name(int(mon[-2].rstrip()[-2::])))
t=len(mon[2].split())
print(mon[2],'\n',' '*3*(7-t),' '.join(str(Gregorian(y, m, i).to_hijri()).split('-')[2] for i in range(1,t+1)),sep='')
for i in mon[3:]:
    print('-'*20+'\n',i,'\n',' '.join(str(Gregorian(y, m, int(j)).to_hijri()).split('-')[2] for j in i.split()),sep='')
