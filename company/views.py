from django.shortcuts import render, redirect, reverse
from .models import Company, AdminProfile
from .forms import RegistrationForm, AdminUpdateForm
# Create your views here.


def view_companies(request):
    user = AdminProfile.objects.get(user=request.user)
    if user.company:
        companies = Company.objects.all()
        args = {'companies': companies}
        return render(request, 'company/home.html', args)
    else:
        args = {'user': user, }
        return render(request, 'company/choose_company.html', args)


def choose_companies(request):
    user = request.user
    args = {'user': user, }
    return render(request, 'company/choose_company.html', args)


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('company:login'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'company/reg_form.html', args)


def update_admin(request):
    if request.method == 'POST':
        user = AdminProfile.objects.get(user=request.user)
        form = AdminUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect(reverse('company:view_companies'))
    else:
        user = AdminProfile.objects.get(user=request.user)
        form = AdminUpdateForm(instance=user)
        args = {'form': form}
        return render(request, 'company/update_admin.html', args)

