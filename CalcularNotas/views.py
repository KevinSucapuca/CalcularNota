from django.shortcuts import render
import math

def home(request):
    nota = None
    resultado = None
    error = None

    if request.method == 'POST':
        nota_raw = request.POST.get('nota')
        opcion = request.POST.get('opcion')

        if not nota_raw:
            error = "Por favor, ingrese una nota"
        else:
            try:
                nota = float(nota_raw)

                if opcion == 'opcion1':
                    if nota >= 0 and nota <= 20:
                        resultado = round((100 * nota) / 20)
                    else:
                        error = "La nota ingresada debe estar entre 0 y 20"
                elif opcion == 'opcion2':
                    if nota >= 0 and nota <= 100:
                        resultado = round((20 * nota) / 100, 2)
                    else:
                        error = "La nota ingresada debe estar entre 0 y 100"
                else:
                    error = "Por favor, seleccione una opción"
            except ValueError:
                error = "El valor ingresado para la nota no es válido"

    return render(request, 'index.html', {'nota': nota, 'resultado': resultado, 'error': error})