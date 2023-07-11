from django.shortcuts import render

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
                    resultado = (100 * nota) / 20
                elif opcion == 'opcion2':
                    resultado = (20 * nota) / 100
                else:
                    error = "Por favor, seleccione una opción"
            except ValueError:
                error = "El valor ingresado para la nota no es válido"

    return render(request, 'index.html', {'nota': nota, 'resultado': resultado, 'error': error})