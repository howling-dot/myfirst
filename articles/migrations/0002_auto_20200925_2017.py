# Generated by Django 3.1.1 on 2020-09-25 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='atricle_text',
            new_name='article_text',
        ),
    ]