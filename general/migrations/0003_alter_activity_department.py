# Generated by Django 3.2.4 on 2021-08-11 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_alter_departmentdetail_head'),
        ('general', '0002_auto_20210810_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='department.departmentdetail'),
        ),
    ]
