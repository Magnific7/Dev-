# Generated by Django 2.2.6 on 2019-11-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0011_auto_20191106_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='levels',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Senior', 'Senior')], default='Beginner', max_length=2),
        ),
    ]
