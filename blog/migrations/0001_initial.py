# Generated by Django 3.0.3 on 2020-03-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(verbose_name='date published')),
                ('post_text', models.CharField(max_length=300)),
            ],
        ),
    ]