# Generated by Django 2.1 on 2021-06-28 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
