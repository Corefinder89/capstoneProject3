# Generated by Django 2.1.5 on 2020-10-22 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20201021_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorinfo',
            old_name='education_field',
            new_name='education_type',
        ),
    ]