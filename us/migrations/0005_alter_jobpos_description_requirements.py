# Generated by Django 4.2.3 on 2023-08-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0004_alter_jobpos_description_advantages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpos',
            name='description_requirements',
            field=models.TextField(blank=True, null=True, verbose_name='نیازمندی ها'),
        ),
    ]
