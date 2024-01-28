# Generated by Django 4.2.9 on 2024-01-27 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_remove_portfolio_image_portfolioimage_portfolio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='your_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='portfolio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_images', to='portfolio_app.portfolio'),
        ),
    ]
