# Generated by Django 4.1 on 2023-04-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='employee',
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='_department', to='department.employee', verbose_name='employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employees', to='department.department', verbose_name='department'),
        ),
    ]