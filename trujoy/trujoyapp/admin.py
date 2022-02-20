from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Event)
admin.site.register(Book_ground)
admin.site.register(Events_list)
admin.site.register(Contact)