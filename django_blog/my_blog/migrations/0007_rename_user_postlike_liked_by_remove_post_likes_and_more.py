# Generated by Django 4.1.2 on 2022-12-17 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0006_postlike_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postlike',
            old_name='user',
            new_name='liked_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.post'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='like',
            field=models.BooleanField(default=False, verbose_name='Like'),
        ),
    ]
