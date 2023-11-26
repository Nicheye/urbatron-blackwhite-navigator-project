from django.contrib import admin



# Register your models here.
from .models import *

# class UserAdminConfig(UserAdmin):
# 	search_fields = ('email','user_name','first_name',)
# 	list_filter = ('email','user_name','first_name','is_active','is_staff',)
# 	ordering = ('-start_date',)
# 	list_display = ('email','user_name','first_name','is_active','is_staff')

# 	fieldsets = (
# 		(None,{'fields':('email','user_name','first_name',)}),
# 		('Permissions',{'fields':('is_staff','is_active')}),
# 		('Personal',{'fields':('about',)}),
# 	)
	

admin.site.register(NewUser)
admin.site.register(City)
admin.site.register(Role)
admin.site.register(CommonPost)
admin.site.register(RecentNew)
admin.site.register(Profile)
admin.site.register(Comment)