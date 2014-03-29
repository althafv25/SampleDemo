from django.contrib import admin
from DemoApp.models import Food,Cuisine,Recipe

admin.site.register(Cuisine)
admin.site.register(Food)
admin.site.register(Recipe)



# from django.contrib import admin
# from owenapp.models import Food,Recipe,Ingredient,FoodImage
#
# admin.site.register(Food)
#
# admin.site.register(FoodImage)
# admin.site.register(Recipe)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('food','amount','recipe')
#
# admin.site.register(Ingredient,IngredientAdmin)