# Generated by Django 2.0.3 on 2018-04-17 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20180415_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='package',
            field=models.ForeignKey(default='5917637d-6d99-4161-ab45-3beeb3dff432', on_delete=django.db.models.deletion.CASCADE, related_name='package_documents', to='document.Package'),
            preserve_default=False,
        ),
    ]
