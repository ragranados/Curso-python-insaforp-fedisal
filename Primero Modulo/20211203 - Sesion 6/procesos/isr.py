def isss(sueldo):
    if sueldo > 1000:
        return 30
    else:
        return sueldo*0.03

def afp(sueldo):
    return sueldo*0.0725

def sueldo_gravable(sueldo):
    return sueldo - isss(sueldo) - afp(sueldo)

def impuesto_isr(sueldo):
    sg = sueldo_gravable(sueldo)

    if sg>0.01 and sg <=472.00:
        return 0
    elif sg>=472.01 and sg<=895.24:
        return (sg - 472.00)*0.1 + 17.67
    elif sg>=895.25 and sg <=2038.10:
        return (sg - 895.24)*0.2 + 60
    elif sg>=2038.11:
        return (sg - 2038.10)-0.3 + 288.57

def descuentos(sueldo):
    return afp(sueldo)+isss(sueldo)+impuesto_isr(sueldo)

def suedo_pagar(sueldo):
    return sueldo - descuentos(sueldo)