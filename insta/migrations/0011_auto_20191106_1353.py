# Generated by Django 2.2.6 on 2019-11-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0010_auto_20191106_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='levels',
            field=models.CharField(choices=[('FR', 'Beginner'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
    ]
