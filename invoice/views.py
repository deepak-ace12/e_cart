from django.shortcuts import render, redirect
from project.models import Item, Project
from .models import Invoice
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from .forms import QuantityForm


def view_invoice(request):
    return render(request, 'invoice/invoice.html')


def cart(request, action, pk):

    item = Item.objects.get(pk=pk)
    if action == 'add':
        Invoice.add_to_cart(item)
    elif action == 'remove':
        Invoice.remove_from_cart(item)
    items = Item.objects.filter(project_id=item.project.pk)
    invoice, created = Invoice.objects.get_or_create(
        project_id=item.project.pk, customer=request.user,
        company=item.project.company
    )
    invoice.customer = request.user
    carts = invoice.cart.all()
    project = Project.objects.get(pk=item.project.pk)
    args = {'items': items, 'carts': carts, 'project': project, }
    return render(request, 'project/items.html', args)


def checkout(request, pk=None):
    if pk:
        invoice, created = Invoice.objects.get(project_id=pk)
    else:
        invoice = request.invoice
    args = {'invoice': invoice, }
    return render(request, 'invoice/checkout.html', args)


def generate_pdf(request):

    invoice, created = Invoice.objects.get_or_create(customer=request.user)
    template = get_template('invoice/invoice.html')
    context = {
        'invoice': invoice,
    }
    html = template.render(context)
    pdf = render_to_pdf('invoice/invoice.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "example_%s.pdf" % ("12341231")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def save_pdf(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def save_qty(request):
    if request.method == 'POST':

        form = QuantityForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse("Some HTML code")

    else:
        form = QuantityForm()

    #This called when we need to display the form: get or error in form fields
    return render('invoice/example.html', {'form': form})

