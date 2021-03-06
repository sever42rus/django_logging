# Generated by Django 4.0 on 2022-03-05 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200, verbose_name='измененная модель')),
                ('record_id', models.PositiveBigIntegerField(verbose_name='ID записи')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи')),
                ('data', models.JSONField(blank=True, default=dict, verbose_name='информация')),
                ('action', models.SmallIntegerField(choices=[(1, 'create'), (2, 'retrive'), (3, 'update'), (4, 'destroy')])),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_changes', to='auth.user', verbose_name='Пользователь')),
            ],
        ),
    ]
