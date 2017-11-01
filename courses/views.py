from django.views.generic.list import ListView
from .models import Course


class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_query_set()
        return qs.filter(owner=self.request.user)

