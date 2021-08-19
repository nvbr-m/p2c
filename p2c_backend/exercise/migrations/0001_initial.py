# Generated by Django 3.2.5 on 2021-08-19 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('instruction', models.TextField()),
                ('pascal_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case', models.CharField(max_length=50)),
                ('expected_result', models.CharField(max_length=50)),
                ('fuck_django_migrations_are_shit', models.CharField(max_length=13)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.task')),
            ],
        ),
    ]