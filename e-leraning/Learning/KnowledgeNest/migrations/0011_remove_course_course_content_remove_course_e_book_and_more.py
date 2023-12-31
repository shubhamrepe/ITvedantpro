# Generated by Django 5.0 on 2023-12-26 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeNest', '0010_student_user_alter_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_content',
        ),
        migrations.RemoveField(
            model_name='course',
            name='e_book',
        ),
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KnowledgeNest.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='e_book',
            field=models.FileField(default=1, upload_to='e_books/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
