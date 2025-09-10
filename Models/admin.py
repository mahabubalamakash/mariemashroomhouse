from django.contrib import admin
from .models import (Group,profile_model,upload_product,send_message,
                     blog_model,home_dalevery_model,kuriar_dalevery_model,
                     upload_videos,)

#-------------Unregister Group Option-----------------#
admin.site.unregister(Group)
#----------------Key Display Admin Panel--------------#
class PROFILE_ADMIN_MANAGER(admin.ModelAdmin):
    list_display = ['id','username','times','dates']
    list_display_links = ['id','username','times','dates']

#-------------Register Model--------------------------#
admin.site.register(profile_model,PROFILE_ADMIN_MANAGER)
admin.site.register(blog_model)
admin.site.register(home_dalevery_model)
admin.site.register(kuriar_dalevery_model)
admin.site.register(upload_product)
admin.site.register(send_message)
admin.site.register(upload_videos)

