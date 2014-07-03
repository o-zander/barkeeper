from django.contrib import admin

from .models import RecipeCategory, Recipe, IngredientCategory, Ingredient, RecipeNeedsIngredient


class RecipeCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecipeCategory, RecipeCategoryAdmin)


class RecipeNeedsIngredientInline(admin.StackedInline):
    model = RecipeNeedsIngredient
    extra = 0


class RecipeAuthor(admin.ModelAdmin):
    inlines = (RecipeNeedsIngredientInline,)

admin.site.register(Recipe, RecipeAuthor)


class IngredientCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(IngredientCategory, IngredientCategoryAdmin)


class IngredientAuthor(admin.ModelAdmin):
    pass

admin.site.register(Ingredient, IngredientAuthor)