from celery import task
from django.core.mail import send_mail
from orders.models import Order
from orders.models import OrderItem


@task
def got_payment(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)

    order_item = OrderItem.objects.get(id=order_id)
    message = 'Dear {},\n\nYou have successfully purchased the following'.format(order.first_name)
    message += "\n\n\t{} x {}(s)".format(order_item.quantity, order_item.product.name)
    message += "\n{}".format(order_item.product.description)
    message += "We look forward to seeing you there."

    mail_sent = send_mail(subject, message, 'kextech@gmx.com', [order.email])
    return mail_sent
