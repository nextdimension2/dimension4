# Generated by Django 3.0.5 on 2020-05-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_apply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc1', models.CharField(default='we', max_length=1000)),
                ('desc2', models.CharField(default='us', max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='apply',
            name='des1',
            field=models.CharField(default='cool', max_length=1000),
        ),
        migrations.AddField(
            model_name='apply',
            name='des2',
            field=models.CharField(default='see', max_length=1000),
        ),
    ]
