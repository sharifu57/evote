# Generated by Django 4.0.3 on 2022-03-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_rename_category_id_nomination_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomination',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AlterField(
            model_name='nomination',
            name='index',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='created_at',
            field=models.TimeField(null=True),
        ),
    ]
