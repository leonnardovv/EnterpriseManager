from django.shortcuts import render
from django.http import HttpResponse
from .models import Enterprise

def home(request):
    template = 'home.html'
    context = locals()

    return render(request, template, context)


def all_enterprises(request):
    template = 'all-enterprises.html'
    all_enterprises = Enterprise.objects.all()
    context = {
        'all_enterprises':all_enterprises,
    }
    # html = ''
    # for enterprise in all_enterprises:
    #     url = '/enterprise/' + str(enterprise.id) + '/'
    #     html += '<a href=" ' + url + '">' + enterprise.name + '</a><br>'

    return render(request, template, context)


def enterprise_details(request, enterprise_id):
    return HttpResponse("Enterprise details: " + str(enterprise_id))
