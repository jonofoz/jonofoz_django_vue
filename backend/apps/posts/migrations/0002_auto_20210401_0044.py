# Generated by Django 3.1.7 on 2021-04-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at', 'updated_at', 'user', 'title', 'body', 'slug']},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug', max_length=200),
            preserve_default=False,
        ),
    ]