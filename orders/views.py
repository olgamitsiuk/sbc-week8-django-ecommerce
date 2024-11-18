from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrderForm()
    
    return render(request, 'orders/order_form.html', {
        'form': form,
        'title': 'Create Order'
    })

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrderForm(instance=order)
    
    return render(request, 'orders/order_form.html', {
        'form': form,
        'title': 'Edit Order'
    })

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('order-list')
        
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
