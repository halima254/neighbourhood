# Generated by Django 3.1.5 on 2021-11-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20211103_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]