# Generated by Django 3.0.8 on 2020-07-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200729_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=78),
            preserve_default=False,
        ),
    ]
