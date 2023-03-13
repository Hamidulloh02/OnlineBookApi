from django.contrib import admin
from .models import Post,Category,Video,Contributor
# Register your models here.
# admin.site.register(Video)
admin.site.register(Contributor)
admin.site.register(Category)
admin.site.register(Post)
