# Generated by Django 3.2.12 on 2023-09-09 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_auto_20230907_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_subscripe', models.DateField(auto_now_add=True, help_text='Дата подписки', verbose_name='дата подписки')),
                ('course', models.ForeignKey(help_text='Курс подписки', on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='courses.course', verbose_name='курс')),
                ('user', models.ForeignKey(help_text='Подписанный пользователь', on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
                'ordering': ('-date_subscripe',),
                'unique_together': {('course', 'user')},
            },
        ),
    ]
