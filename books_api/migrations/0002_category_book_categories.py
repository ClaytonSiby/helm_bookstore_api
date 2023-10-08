# Generated by Django 4.2.6 on 2023-10-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='books_api.category'),
        ),
    ]
