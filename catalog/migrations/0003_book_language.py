# Generated by Django 2.2 on 2019-04-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190428_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]