# Generated by Django 3.0.4 on 2021-01-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210118_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link above to read th blog post', max_length=100),
        ),
    ]
