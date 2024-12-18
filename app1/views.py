from django.shortcuts import render
from .models import MstrCustlist  # Replace with actual model name
from django.http import HttpResponse
from .models import Treatables

# Create your views here.
#def master_customer_list(request):
    #master_customer_list = MstrCustlist.objects.all()  # Query the existing table
   # return render(request, 'myapp/treatables.html', {'data': master_customer_list})

def treatables_list(request):
    treatables_list = Treatables.objects.all()  # Query the existing table
    return render(request, 'myapp/treatables.html', {'data': treatables_list})

# def index(request):
#     return HttpResponse("Hello from app1!")

def index(request):
    # Render the index.html template from the app1/templates/app1 folder
    data = Treatables.objects.all()  # Query the existing table
    return render(request, 'myapp/treatables.html', {'data':data})