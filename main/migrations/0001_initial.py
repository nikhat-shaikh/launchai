# Generated by Django 3.2.16 on 2024-08-02 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('startup_idea', models.TextField(blank=True, null=True)),
                ('target_number_of_users_goal', models.IntegerField(blank=True, default=0, null=True)),
                ('target_date_goal', models.DateField(blank=True, null=True)),
                ('generated_idea', models.TextField(blank=True, null=True)),
                ('generated_slogan', models.TextField(blank=True, null=True)),
                ('generated_problem', models.TextField(blank=True, null=True)),
                ('generated_solution', models.TextField(blank=True, null=True)),
                ('generated_user_persona', models.TextField(blank=True, null=True)),
                ('generated_market_analysis', models.TextField(blank=True, null=True)),
                ('generated_mvp_builder', models.TextField(blank=True, null=True)),
                ('generated_user_feedback_analyzer', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
