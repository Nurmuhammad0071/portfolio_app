# Generated by Django 4.2.9 on 2024-01-23 20:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_alter_basemodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('your_name', models.ImageField(upload_to='portfolio')),
                ('your_email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(max_length=255)),
                ('finished', models.DateField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('image', models.ImageField(upload_to='portfolio')),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('about_title', models.CharField(max_length=255)),
                ('happy_clients', models.IntegerField()),
                ('projects', models.IntegerField()),
                ('support', models.IntegerField()),
                ('workers', models.IntegerField()),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('knowledge', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('image', models.ImageField(upload_to='portfolio')),
                ('name', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('portfolio_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio_app.basemodel')),
                ('name', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('project_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('project_url', models.URLField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio_app.category')),
                ('image', models.ManyToManyField(blank=True, to='portfolio_app.portfolioimage')),
            ],
            bases=('portfolio_app.basemodel',),
        ),
    ]