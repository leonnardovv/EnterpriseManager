from django.shortcuts import render

def index(request):
    context = locals()
    template = 'index.html'
    return render(request, template, context)
