# Generated by Django 5.0.4 on 2024-06-18 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_sentence_containedwords_sentence_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.lesson'),
        ),
    ]