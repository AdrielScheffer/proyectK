# Generated by Django 4.0.6 on 2022-12-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_autists_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autists',
            name='badOpinion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='autists',
            name='goodOpinion',
            field=models.TextField(),
        ),
    ]
