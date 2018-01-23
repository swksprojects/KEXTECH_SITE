from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
from .tasks import got_payment
from orders.dispatch import OrderDispatcher


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)

        # mark the order as paid
        order.paid = True
        order.save()

        dispatcher = OrderDispatcher()
        dispatcher.dispatch(order)

        got_payment.delay(order.id)


valid_ipn_received.connect(payment_notification)

