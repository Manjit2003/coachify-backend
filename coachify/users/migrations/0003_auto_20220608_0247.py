# Generated by Django 3.2.13 on 2022-06-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220608_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='parent',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='parent',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='student',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='student',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='last name'),
        ),
    ]
