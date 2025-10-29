


dias_al_gimnasio = [1, 3, 4, 0, 2]  # Lista con los días que diferentes personas van al gimnasio

try:
    # Calcular el promedio de los días registrados
    promedio_dias = sum(dias_al_gimnasio) / len(dias_al_gimnasio)
except ZeroDivisionError:
    # Si la lista está vacía, el promedio no se puede calcular
    promedio_dias = 0.0

print("Promedio de días al gimnasio:", promedio_dias)