from django.contrib import admin

from . import models

# Register your models here.



admin.site.register(models.Article)
admin.site.register(models.Ourproducts)
admin.site.register(models.Ourservices)
admin.site.register(models.Oursolutions)

admin.site.site_header = "مدیریت وبسایت"