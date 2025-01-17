from django.shortcuts import render
from .models import MstrCustlist  # Replace with actual model name
from django.http import HttpResponse
from .models import Treatables

# Create your views here.
#def master_customer_list(request):
    #master_customer_list = MstrCustlist.objects.all()  # Query the existing table
   # return render(request, 'treatables_view/treatables.html', {'data': master_customer_list})

def treatables_list(request):
    treatables_list = Treatables.objects.all()  # Query the existing table
    return render(request, 'view_treatables/treatables.html', {'data': treatables_list})

# def index(request):
#     return HttpResponse("Hello from view_treatables!")

def index(request):
    # Render the index.html template from the view_treatables/templates/view_treatables folder
    data = Treatables.objects.all()  # Query the existing table
    return render(request, 'view_treatables/treatables.html', {'data':data})