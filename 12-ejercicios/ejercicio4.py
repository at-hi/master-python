"""
Programa que compruebe si una variable esta vacia,
y si esta vacia, rellenarla con texto en minusculas
y mostrarlo en mayusculas.
"""

text = ""
if len(text.strip()) <= 0:
    text = "Hi, \U0001F44B  I'm a lowercases text!"
    print(text.upper())
else:
    print(f"The variable has content:  {text}")
