# Generated by Django 4.1 on 2022-10-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapps', '0004_likepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default='BlankPic.jpg', upload_to='profile_images'),
        ),
    ]
