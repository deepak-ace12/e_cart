from django.shortcuts import render, redirect
from .models import Project, Item
from invoice.models import Invoice


def view_projects(request, pk=None):
    if pk:
        projects = Project.objects.filter(company_id=pk)
    else:
        projects = request.company
    args = {'projects': projects, }
    return render(request, 'project/projects.html', args)


def view_items(request, pk=None):
    if pk:
        items = Item.objects.filter(project_id=pk)
    else:
        items = request.project
    project = Project.objects.get(pk=pk)
    invoice, created = Invoice.objects.get_or_create(
        project_id=pk, customer_id=request.user.pk,
        company=project.company
    )

    args = {'items': items, 'project': project, 'invoice': invoice }
    return render(request, 'project/items.html', args)

