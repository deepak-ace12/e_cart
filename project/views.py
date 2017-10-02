from django.shortcuts import render, redirect
from .models import Project, Item


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
    args = {'items': items, 'project': project, }
    return render(request, 'project/items.html', args)

