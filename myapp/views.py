from django.shortcuts import render

def my_view(request):
    context = {'name': 'World'}
    return render(request, "my_static_page.html", context)