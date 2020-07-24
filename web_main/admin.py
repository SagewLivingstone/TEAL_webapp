from django.contrib import admin

from .models import County, Owner, Land, LandImprovement


admin.site.register(County)
admin.site.register(Owner)
admin.site.register(Land)
admin.site.register(LandImprovement)
