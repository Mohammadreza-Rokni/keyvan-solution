# Generated by Django 4.2 on 2023-08-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reference',
            field=models.TextField(default=False, verbose_name='منابع'),
        ),
    ]
