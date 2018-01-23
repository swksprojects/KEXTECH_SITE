from courses.models import Course
from django.contrib.auth.models import User


class OrderDispatcher(object):

    def __init__(self):
        pass

    def dispatch(self, order):
        if order.username is not None:
            for item in order.items.all():
                if item.product.online_course_dispatch:
                    self.enroll_user_in_online_course(item.product_id, order.username)

    @staticmethod
    def enroll_user_in_online_course(product_id, username):
        course = Course.objects.filter(product_id=product_id)[0]
        user = User.objects.filter(username=username)[0]
        course.students.add(user)
        course.save()


