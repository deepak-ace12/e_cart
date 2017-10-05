from django.shortcuts import render, redirect, reverse
from .models import Company
from .forms import RegistrationForm
# Create your views here.


def view_companies(request):
    companies = Company.objects.all()
    args = {'companies': companies}
    return render(request, 'company/home.html', args)


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('company:view_companies'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'company/reg_form.html', args)

