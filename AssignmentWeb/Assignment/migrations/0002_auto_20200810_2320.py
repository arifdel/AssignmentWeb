# Generated by Django 3.1 on 2020-08-10 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcat',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Assignment.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Assignment.subcategory'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Assignment.category'),
        ),
    ]