from django.contrib import admin
from .models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Mobile","Message")
admin.site.register(contactus,contactusAdmin)


class igalleryAdmin(admin.ModelAdmin):
    list_display = ('gname','gpic')
admin.site.register(igallery,igalleryAdmin)


################################################
class ncategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category','cpic','cdate')
admin.site.register(ncategory,ncategoryAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','cpic','cdate')
admin.site.register(city,cityAdmin)


class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic')
admin.site.register(slider,sliderAdmin)

class mynewsAdmin(admin.ModelAdmin):
    list_display = ('id','ntitle','nhead','ndes','ncity','category','ndate','npic')
admin.site.register(mynews,mynewsAdmin)


class videonewsAdmin(admin.ModelAdmin):
    list_display =('id','vlink','vhead','vcategory','vcity','vdate','vdec')
admin.site.register(videonews,videonewsAdmin)