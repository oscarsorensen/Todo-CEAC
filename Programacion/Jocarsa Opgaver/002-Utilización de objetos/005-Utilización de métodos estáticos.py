

class Entrenamiento:
    # Propiedades estáticas (atributos de clase)
    max_repeticiones = 0
    factor_calidad = 0.0

    @staticmethod
    def CalcularCalificacion(series, repeticiones):
        # Si las repeticiones son menores que max_repeticiones
        if repeticiones < Entrenamiento.max_repeticiones:
            return series * repeticiones
        else:
            return (series * repeticiones) + Entrenamiento.factor_calidad


# Programa principal
if __name__ == "__main__":
    # Inicialización de propiedades estáticas
    Entrenamiento.max_repeticiones = 12
    Entrenamiento.factor_calidad = 5.5

    # Uso del método estático
    series = 4
    repeticiones = 15

    calificacion = Entrenamiento.CalcularCalificacion(series, repeticiones)
    print("Calificación del entrenamiento:", calificacion)
