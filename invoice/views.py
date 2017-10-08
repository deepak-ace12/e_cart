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

    sum = 0
    user = AdminProfile.objects.get(user=request.user)
    quantity = Quantity.objects.filter(invoice_id=pk)
    adjustment = Adjustment.objects.get(invoice_id=pk)
    cart_info1 = zip(invoice.cart.all(), quantity)
    cart_info = zip(invoice.cart.all(), quantity, range(len(quantity)))
    for cart, qty in cart_info1:
        sum = sum + (qty.quantity * cart.unit_price)
    invoice.total = sum
    invoice.save()
    args = {'invoice': invoice, 'user': user, 'cart_info': cart_info,
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
    user = AdminProfile.objects.get(user=request.user)
    quantity = Quantity.objects.filter(invoice_id=pk)
    adjustment = Adjustment.objects.get(invoice_id=pk)
    cart_info = zip(invoice.cart.all(), quantity, range(len(quantity)))
    template = get_template('invoice/invoice.html')
    context = {
        'invoice': invoice, 'user': user, 'cart_info': cart_info,
        'adjustment': adjustment,
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


def save_qty(request, pk=None):
    invoice = Invoice.objects.get(pk=pk)
    carts = invoice.cart.all()

    for item in carts:
        qty, created = Quantity.objects.get_or_create(invoice=invoice, item=item)
        if request.method == 'POST':
            form = QuantityForm(request.POST, instance=qty)
            args = {'form': form, 'invoice': invoice}
            if form.is_valid():
                form.save()
            return render(request, 'invoice/checkout.html', args)
        else:
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
