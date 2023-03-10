# Generated by Django 4.1.3 on 2023-01-10 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_rename_team_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='Staff_pic',
            new_name='Staff_Pic',
        ),
        migrations.AlterField(
            model_name='staff_social',
            name='Facebook',
            field=models.URLField(blank=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='staff_social',
            name='Instagram',
            field=models.URLField(blank=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='staff_social',
            name='Linkedin',
            field=models.URLField(blank=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='staff_social',
            name='Twitter',
            field=models.URLField(blank=True, verbose_name='Twitter'),
        ),
    ]
