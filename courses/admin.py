from django.contrib import admin
from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInLine(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'owner', 'available', 'slug', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview', 'available']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInLine]
    filter_horizontal = ('students',)

    # owner = models.ForeignKey(User, related_name='course_created')
    # subject = models.ForeignKey(Subject, related_name='courses')
    # title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)
    # overview = models.TextField()
    # created = models.DateTimeField(auto_now_add=True)
    # students = models.ManyToManyField(User, related_name='courses_enrolled', blank=True)
    #available = models.BooleanField(default=True)