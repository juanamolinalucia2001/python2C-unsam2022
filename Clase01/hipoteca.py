#ejercicio 1.11 corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado. 
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pagoExtra=1000

#mientras deuda sea mayor a 0 
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

    if saldo < 0:
        total_pagado+=saldo
        saldo=0.0

    elif (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        total_pagado = total_pagado + pagoExtra
    
    mes =+ 1
    print(mes,"Pagado:", round(total_pagado, 2), "Su deuda es de: ",round(saldo,2))
