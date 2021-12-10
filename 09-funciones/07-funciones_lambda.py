"""Se definen en una linea y se usa para tareas concretas"""

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034)) 

# DA: Un código para definir el valor total + iva

precio_final = lambda precio: f"El valor + iva es {precio / 100*19}"
print(precio_final(20000))