# Generated by Django 2.1.7 on 2019-03-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190308_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
