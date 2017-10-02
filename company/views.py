from django.shortcuts import render, HttpResponse
from .models import Company
# Create your views here.


def view_companies(request):
    companies = Company.objects.all()
    args = {'companies': companies}
    return render(request, 'company/home.html', args)
