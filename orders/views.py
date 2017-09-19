from django.shortcuts import render, redirect#, get_object_or_404
from django.core.urlresolvers import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart


def order_create(request):
    print("creating orders...")
    cart = Cart(request)
    if request.method == 'POST':
        print("This is a post reques")
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print("The Form is Valid")
            order = form.save()
            for item in cart:
                print("item")
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            print("created orders")
            # # clear the cart
            # cart.clear()
            # # launch asynchronous task
            # order_created.delay(order.id)
            # return render(request, 'orders/order/created.html', {'order': order})

            # clear the cart
            cart.clear()
            print("cart clear")
            # launch asynchronous task
            order_created.delay(order.id)
            print("orders sent to other process")
            # set the order in the session
            request.session['order_id'] = order.id
            print("order id" + str(order.id))
            # redirect to the payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
