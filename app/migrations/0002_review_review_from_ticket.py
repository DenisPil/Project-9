# Generated by Django 4.0.1 on 2022-01-06 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_from_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ticket'),
        ),
    ]
