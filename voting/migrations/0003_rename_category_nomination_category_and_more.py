# Generated by Django 4.0.3 on 2022-03-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_alter_nomination_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomination',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='nomination',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
