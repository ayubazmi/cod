# Generated by Django 3.2.2 on 2021-07-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Freakin BlogPost!', max_length=255),
        ),
    ]