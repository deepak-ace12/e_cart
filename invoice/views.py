from django.shortcuts import render, redirect, reverse
from project.models import Item, Project
from .models import Invoice, Quantity, Adjustment
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from django.http import HttpResponse
from .utils import render_to_pdf
from .forms import QuantityForm, AdjustmentForm
from company.models import AdminProfile


def view_invoice(request, pk=None):
    if pk:
        invoice = Invoice.objects.get(pk=pk)
    else:
        invoice = request.invoice
    user = AdminProfile.objects.get(user=request.user)
    quantity, created = Quantity.objects.get_or_create(invoice_id=pk)
    adjustment = Adjustment.objects.get(invoice_id=pk)

    args = {'invoice': invoice, 'user': user, 'quantity': quantity,
            'adjustment': adjustment,
            }
    return render(request, 'invoice/invoice.html', args)


def cart(request, action, pk):

    item = Item.objects.get(pk=pk)
    if action == 'add':
        Invoice.add_to_cart(item, request.user)
    elif action == 'remove':
        Invoice.remove_from_cart(item, request.user)
    items = Item.objects.filter(project_id=item.project.pk)
    invoice, created = Invoice.objects.get_or_create(
        project_id=item.project.pk, customer_id=request.user.pk,
        company=item.project.company
    )
    carts = invoice.cart.all()
    project = Project.objects.get(pk=item.project.pk)
    args = {'items': items, 'carts': carts, 'project': project, 'invoice': invoice}
    return render(request, 'project/items.html', args)


def checkout(request, pk=None):
    if pk:
        invoice = Invoice.objects.get(pk=pk)
    else:
        invoice = request.invoice
    args = {'invoice': invoice}
    return render(request, 'invoice/checkout.html', args)


def generate_pdf(request, pk=None):
    if pk:
        invoice = Invoice.objects.get(pk=pk)
    else:
        invoice = request.invoice
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


def save_qty(request, pk=None):
    invoice = Invoice.objects.get(pk=pk)
    if pk:
        qty, created = Quantity.objects.get_or_create(invoice=invoice)
    else:
        qty = request.invoice

    if request.method == 'POST':
        form = QuantityForm(request.POST, instance=qty)
        args = {'form': form, 'invoice': invoice}
        if form.is_valid():
            form.save()
        return render(request, 'invoice/checkout.html', args)
    else:
        invoice = Invoice.objects.get(pk=pk)
        qty, created = Quantity.objects.get_or_create(invoice=invoice)
        form = QuantityForm(instance=qty)
        args = {'form': form, 'invoice': invoice}
        return render(request, 'invoice/checkout.html', args)


def adjustment(request, pk=None):
    invoice = Invoice.objects.get(pk=pk)
    if pk:
        amt, created = Adjustment.objects.get_or_create(invoice=invoice)
    else:
        amt = request.invoice

    if request.method == 'POST':
        form = AdjustmentForm(request.POST, instance=amt)
        args = {'form': form, 'invoice': invoice}
        if form.is_valid():
            form.save()
        return render(request, 'invoice/checkout.html', args)
    else:
        invoice = Invoice.objects.get(pk=pk)
        amt, created = Adjustment.objects.get_or_create(invoice=invoice)
        form = AdjustmentForm(instance=amt)
        args = {'form': form, 'invoice': invoice}
        return render(request, 'invoice/adjustment.html', args)
