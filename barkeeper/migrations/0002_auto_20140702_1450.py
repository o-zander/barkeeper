# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Ingredient Category',
                'verbose_name_plural': 'Ingredient Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Recipe Category',
                'verbose_name_plural': 'Recipe Categories',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='recipeneedsingredient',
            options={'verbose_name': 'Recipe Ingredient', 'verbose_name_plural': 'Recipe Ingredients'},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(default=0, verbose_name='Category', to='barkeeper.IngredientCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(default=0, verbose_name='Category', to='barkeeper.RecipeCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeneedsingredient',
            name='ingredient',
            field=models.ForeignKey(verbose_name='Ingredient', to='barkeeper.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeneedsingredient',
            name='recipe',
            field=models.ForeignKey(verbose_name='Recipe', to='barkeeper.Recipe'),
        ),
    ]
