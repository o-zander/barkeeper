from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RecipeCategory(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Recipe Category')
        verbose_name_plural = _('Recipe Categories')

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    category = models.ForeignKey(RecipeCategory, verbose_name=_('Category'))
    description = models.TextField(_('Description'))
    instructions = models.TextField(_('Instructions'))

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')

    def __unicode__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Ingredient Category')
        verbose_name_plural = _('Ingredient Categories')

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    category = models.ForeignKey(IngredientCategory, verbose_name=_('Category'))

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')

    def __unicode__(self):
        return self.name


class RecipeNeedsIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name=_('Recipe'))
    ingredient = models.ForeignKey(Ingredient, verbose_name=_('Ingredient'))
    amount = models.PositiveIntegerField(_('Amount'), help_text=_('in ml'))

    class Meta:
        verbose_name = _('Recipe Ingredient')
        verbose_name_plural = _('Recipe Ingredients')

    def __unicode__(self):
        return '%i ml %s' % (self.amount, self.ingredient)
