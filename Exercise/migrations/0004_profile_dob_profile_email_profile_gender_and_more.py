# Generated by Django 4.0.1 on 2022-03-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0003_profile_delete_dob_delete_email_delete_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
