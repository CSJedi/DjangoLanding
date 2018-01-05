from django.shortcuts import render

def procedure_list(request):
    return render(request, 'landing/procedure_list.html')