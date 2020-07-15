# Generated by Django 3.0.8 on 2020-07-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('pub_date_blog', models.CharField(max_length=30)),
                ('blog_image', models.ImageField(upload_to='images/')),
                ('body', models.CharField(max_length=500)),
            ],
        ),
    ]
