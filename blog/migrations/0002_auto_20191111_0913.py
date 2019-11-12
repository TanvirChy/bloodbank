# Generated by Django 2.2.7 on 2019-11-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='Only Bangladesh', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='blood',
            field=models.TextField(default='Need blood group is:-'),
        ),
        migrations.AddField(
            model_name='post',
            name='medical',
            field=models.CharField(default='Now we are in ', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
