# Generated by Django 4.2.4 on 2023-08-18 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_comments', to='home.blogpost'),
        ),
    ]
