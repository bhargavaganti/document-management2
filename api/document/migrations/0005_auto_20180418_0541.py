# Generated by Django 2.0.3 on 2018-04-18 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_document_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_document', to='document.Package'),
        ),
    ]
