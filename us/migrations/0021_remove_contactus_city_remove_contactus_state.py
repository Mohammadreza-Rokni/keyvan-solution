# Generated by Django 4.2.3 on 2023-08-30 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0020_remove_contactus_fild_of_activity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='city',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='state',
        ),
    ]
