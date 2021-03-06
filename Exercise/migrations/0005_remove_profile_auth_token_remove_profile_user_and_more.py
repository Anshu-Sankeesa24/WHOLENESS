# Generated by Django 4.0.1 on 2022-03-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0004_profile_dob_profile_email_profile_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='auth_token',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
