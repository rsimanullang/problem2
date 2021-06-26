num=int(input('Enter a three digit number\t:'))
if ((num<100) | (num>999)):
    print('You have not entered a number between 100 and 999')
else:
    flag=0
    o=num%10
    t=int(num/10)%10
    h=int(num/100)%10
    print('o\t:', str (o), 't\t:',str(t),'h\t:',str(h))
    rev=h+t*10+o*100
    print('Number obtained by reversing the order of the digits\t:',str(rev))
    suml=num+rev
    print('Sum of the number and that obtained by reversing the order of digits \t:', str(suml))
    if suml<1000:
        ol=suml%10
        tl=int(suml/10)%10
        hl=int(suml/100)%10
        print('ol\t:',str(ol),'tl\t:', str(tl),'hl\t:',str(hl))
    if ((o==ol)|(o==tl)|(o==hl)|(t==ol)|(t==tl)|(t==hl)|(h==ol)|(h==tl)|(h==hl)):
        print('Condition true')
        flag==1
    else:
        ol=suml%10
        tl=int(suml/10)%10
        hl=int(suml/100)%10
        thl=int(suml/1000)%10
        print('ol\t:',str(ol),'tl\t:',str(tl),'hl\t:',str(hl),'tl\t:',str(tl))
    if ((o==ol)|(o==tl)|(o==hl)|(o==thl)|(t==ol)|(t==tl)|(t==hl)|(t==thl)|(h==ol)|(h==tl)|(h==hl)|(h==thl)):
        print('Condition true')
        flag==1