# Generated by Django 4.1.3 on 2022-12-04 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import supermarket.models.store_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('uuid_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.uuid')),
                ('type', models.CharField(max_length=150, unique=True)),
                ('valid_name', models.BooleanField(default=False)),
            ],
            bases=('core.uuid',),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('uuid_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.uuid')),
                ('name', models.CharField(max_length=155, unique=True)),
                ('store_type', models.CharField(max_length=100)),
                ('image', models.FileField(default='default.png', upload_to=supermarket.models.store_model.store_files_path)),
                ('is_verified', models.BooleanField(default=False)),
                ('location', models.JSONField(blank=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supermarket.types')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.uuid',),
        ),
    ]
