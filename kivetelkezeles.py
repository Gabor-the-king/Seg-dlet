def terulet(a,b):
    ter=a*b
    if ter<100:
        raise ValueError('Hiba: Túl kicsi a telek!')
    return ter

print("feladat: Terület számítás")
while True:
    a=float(input('Kérem adja meg a telek szélességét (a): '))
    if a==-1:
        break
    b=float(input('Kérem adja meg a telek hosszúságát (b): '))
    if a==-1:
        break
    try:
        print(f'Telek területe: {terulet(a,b)} m2')
    except ValueError as error:
        print(error)
