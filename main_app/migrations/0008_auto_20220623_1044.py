# Generated by Django 3.0.3 on 2022-06-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200118_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='State_Medical_Council',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='registration_no',
            field=models.IntegerField(),
        ),
    ]
