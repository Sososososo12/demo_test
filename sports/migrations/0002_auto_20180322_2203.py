# Generated by Django 2.1 on 2018-03-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='paperauthororg',
            field=models.CharField(max_length=200, null=True, verbose_name='文献作者隶属组织'),
        ),
    ]
