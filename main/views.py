from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname': 'NarwhllShop',
        'name': 'Davin Fauzan Akmalianto',
        'npm': '2406409504'
    }

    return render(show_main, "main.html", context)