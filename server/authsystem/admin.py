from django.contrib import admin
from .models import User, Photos
from django.utils.safestring import mark_safe

class UserAdmin(admin.ModelAdmin):
    fields = (
        'id', 'username', 'name', 'surname', 'group', 
        'email', 'is_active', 'is_staff', 'is_superuser', 
    )
    list_display = (
        'id', 'name', 'surname', 'group', 'email', 
    )
    search_fields = (
        'id', 'username', 'name', 'surname', 'group', 
        'email', 'is_active', 'is_staff', 'is_superuser', 
    )
    readonly_fields = (
        'id',
    )

class PhotosAdmin(admin.ModelAdmin):
    fields = (
        'id', 'user', 'photo', 
    )
    list_display = (
        'id', 'user', 'get_photo', 
    )
    search_fields = (
        'id', 'user', 
    )
    readonly_fields = (
        'id',
    )

    def get_photo(self, obj):
        if obj.photo:
            print(obj.photo.url)
            return mark_safe(f'<img src="{obj.photo.url}", width=50, height=50></img>')
        else:
            return 'photo'


admin.site.register(User, UserAdmin)
admin.site.register(Photos)