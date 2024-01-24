# Generated by Django 4.2.9 on 2024-01-23 19:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('image', models.FileField(upload_to='images')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('website', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('freelance', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('map', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
    ]
