# Generated by Django 3.1.7 on 2021-04-01 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210401_0219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id', 'created_at', 'updated_at', 'user_id', 'title', 'body', 'slug']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
