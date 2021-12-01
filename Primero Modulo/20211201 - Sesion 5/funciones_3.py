# programa pra valores por default

#pueden o no ir, son opcionales


def calculo_descuentos(sueldo: float, isss: float=0.03,afp: float=0.0725)->float:
    """
    La funcion realiza el calculo de descuentos de isss y afp con base al sueldo
    sueldo: parametro usado apra calculo de descuentos
    isss: parametro opcional (default: 3%)
    afp: aprametro opcional (default: 7.25%)
    el valor de retorno es la suma de apf e isss
    """
    desc = sueldo*isss+sueldo*afp
    return desc

descuentos = calculo_descuentos(1000)
print(descuentos)
descuentos2 =  calculo_descuentos(1000, 0.04)
print(descuentos2)