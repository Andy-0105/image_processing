def people(i):
    x=((350+180)*i)*1.1
    return round(x,1)
def box(b):
    if b<=3:
        c=350
        return round((c*3+138*b)*1.1,1)
    if b>=4 and b<=6:
        c=490
        return (c*3+138*b)*1.1
    if b>=7 and b<=9:
        c=630
        return (c*3+138*b)*1.1
    if b>=10 and b<=12:
        c=770
        return (c*3+138*b)*1.1
    if b>=13 and b<=15:
        c=910
        return (c*3+138*b)*1.1
    if b>15:
        c=1260
        return round((c*3+138*b)*1.1,1)
