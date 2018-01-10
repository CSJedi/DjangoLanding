from django.shortcuts import render
from .models import DelyveryInfo, ProcedureInfo

def index(request):
	delyverys = DelyveryInfo.objects.all()
	procedures = ProcedureInfo.objects.all()
	return render(request, 'landing/index.html', {'delyverys': delyverys, 'procedures': procedures } )