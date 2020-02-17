# Generated by Django 2.2.9 on 2020-01-28 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields
import django_multitenant.mixins

from django_multitenant.db import migrations as tenant_migrations


def get_operations():
    operations = [
        migrations.CreateModel(
            name='ModelConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='tests.Account')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='tests.Employee')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),

        migrations.RunSQL("ALTER TABLE tests_modelconfig DROP CONSTRAINT tests_modelconfig_pkey CASCADE;"),
        migrations.RunSQL("ALTER TABLE tests_modelconfig ADD CONSTRAINT tests_modelconfig_pkey PRIMARY KEY (account_id, id);"),
    ]

    if settings.USE_CITUS:
        operations += [tenant_migrations.Distribute('ModelConfig'),]

    return operations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('tests', '0017_auto_20200128_0853'),
    ]

    operations = get_operations()
