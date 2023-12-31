# Generated by Django 4.2.4 on 2023-08-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_tiger_park_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='TigerPark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_employee', models.IntegerField()),
                ('clients', models.TextField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='tiger_park',
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='student',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='abd@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
