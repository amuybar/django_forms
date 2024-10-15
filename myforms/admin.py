from django.contrib import admin

from myforms.models import Contact, Post


# CUSTOMIZING THE ADMIN VIEW
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


#   REGISTERING THE CONTACT MODEL WITH ITS CUSTOMIZED VIEW
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post)
