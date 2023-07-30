from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone','email','my_place')

class WebAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('one_topic', 'level')
    
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name','email')


    



admin.site.register(Order,OrderAdmin)
admin.site.register(Webpack,WebAdmin)
admin.site.register(About)
admin.site.register(Faq)
admin.site.register(Apply)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Profile)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Problem)
admin.site.register(Price)
admin.site.register(New)
admin.site.register(Password,PasswordAdmin)