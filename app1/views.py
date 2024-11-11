from django.shortcuts import render
from .models import MstrCustlist  # Replace with actual model name
from django.http import HttpResponse

# Create your views here.
def master_customer_list(request):
    master_customer_list = MstrCustlist.objects.all()  # Query the existing table
    return render(request, 'myapp/master_customer_list.html', {'data': master_customer_list})

# def index(request):
#     return HttpResponse("Hello from app1!")

def index(request):
    # Render the index.html template from the app1/templates/app1 folder
    data = MstrCustlist.objects.all()  # Query the existing table
    return render(request, 'myapp/master_customer_list.html', {'data':data})