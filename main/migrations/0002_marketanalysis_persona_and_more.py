# Generated by Django 5.0.7 on 2024-08-03 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demographics_age', models.IntegerField(max_length=255)),
                ('demographics_gender', models.BooleanField(max_length=255)),
                ('demographics_location', models.CharField(max_length=255)),
                ('demographics_occupation', models.CharField(max_length=255)),
                ('demographics_salary', models.FloatField()),
                ('pain_points', models.TextField(blank=True, null=True)),
                ('core_needs', models.TextField(blank=True, null=True)),
                ('motivation', models.TextField(blank=True, null=True)),
                ('behavior', models.TextField(blank=True, null=True)),
                ('quote', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='startupproject',
            name='generated_user_persona',
        ),
        migrations.AlterField(
            model_name='startupproject',
            name='generated_market_analysis',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.marketanalysis'),
        ),
        migrations.AddField(
            model_name='startupproject',
            name='generated_persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.persona'),
        ),
    ]
