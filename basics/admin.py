from basics.models import User
from django.contrib import admin
class PollAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question', 'pub_date', 'was_published_today')
admin.site.register(User)
