# Generated by Django 4.2.4 on 2023-08-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_student_age_alter_student_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='contact_number',
            field=models.CharField(default='123456789', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='John', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Doe', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default='123 Main St, City'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=100),
        ),
    ]
