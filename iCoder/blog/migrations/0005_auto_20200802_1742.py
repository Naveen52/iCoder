# Generated by Django 3.0.8 on 2020-08-02 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomments',
            old_name='id',
            new_name='sno',
        ),
    ]
