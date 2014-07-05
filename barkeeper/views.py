from django.views.generic import TemplateView, ListView

from .models import Recipe, Ingredient


class IndexView(TemplateView):
    template_name = 'index.html'


class RecipesView(ListView):
    model = Recipe
    template_name = 'recipe/list.html'

    def get_context_data(self, **kwargs):
        kwargs.update(view_name='recipes')
        return super(RecipesView, self).get_context_data(**kwargs)


class IngredientsView(ListView):
    model = Ingredient
    template_name = 'ingredient/list.html'

    def get_context_data(self, **kwargs):
        kwargs.update(view_name='ingredients')
        return super(IngredientsView, self).get_context_data(**kwargs)