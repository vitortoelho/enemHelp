# Generated by Django 5.1.2 on 2024-11-10 21:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dadosQuiz', '0005_alter_alternativa_questoes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resultado', to=settings.AUTH_USER_MODEL),
        ),
    ]
