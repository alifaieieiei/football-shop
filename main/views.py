from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Alifa Izzatunnisa Elqudsi Prabowo',
        'npm': '2406365212',
        'class': 'PBD KKI'
    }

    return render(request, "main.html", context)