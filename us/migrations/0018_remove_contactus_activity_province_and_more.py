# Generated by Django 4.2.1 on 2023-08-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0017_otp_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='activity_province',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='degree_of_education',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='field_of_study',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='history',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='text',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='title',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='type_of_cooperation',
        ),
        migrations.AddField(
            model_name='contactus',
            name='address',
            field=models.TextField(default=2, verbose_name='آدرس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='cellular_phone',
            field=models.CharField(default=2, max_length=11, verbose_name='تلفن همراه'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='city',
            field=models.CharField(default=2, max_length=200, verbose_name='شهر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default=2, max_length=254, verbose_name='ایمیل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='landlineـphone',
            field=models.CharField(default=2, max_length=11, verbose_name=' تلفن ثابت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='prudoct',
            field=models.CharField(default=2, max_length=200, verbose_name='محصول / خدمات'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='state',
            field=models.CharField(default=2, max_length=200, verbose_name='استان'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='field_of_activity',
            field=models.CharField(max_length=200, verbose_name='زمینه فعالیت'),
        ),
    ]