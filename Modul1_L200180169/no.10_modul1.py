# Nomer 10
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D == 0 :
        return "determinan nol. Persamaan mempunyai satu akar kembar"
    elif D > 0 :
        return  "determinan positif. Persamaan mempunyai akar real"
    elif D < 0 :
        return "determinan negatif. Persamaan mempunyai akar real"
