# Generated by Django 4.2.1 on 2023-08-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0018_remove_contactus_activity_province_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='field_of_activity',
            new_name='area_of_activity',
        ),
        migrations.AddField(
            model_name='contactus',
            name='fild_of_activity',
            field=models.CharField(choices=[('Product', 'Product'), ('Services available', 'Services available')], default=1, max_length=200, verbose_name='حوضه فعالیت'),
            preserve_default=False,
        ),
    ]
