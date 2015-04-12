from django.contrib import admin

from website.models import FoodItem, Feedback, MenuDocs


admin.site.register(FoodItem)
admin.site.register(Feedback)
admin.site.register(MenuDocs)
