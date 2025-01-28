# Generated by Django 4.2.18 on 2025-01-27 16:42

from django.db import migrations, models
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0027_attributeoption_code_attributeoptiongroup_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCustomProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug')),
                ('requires_shipping', models.BooleanField(default=True, verbose_name='Requires shipping?')),
                ('track_stock', models.BooleanField(default=True, verbose_name='Track stock levels?')),
                ('another_text', models.CharField(blank=True, max_length=300, null=True)),
                ('options', models.ManyToManyField(blank=True, to='catalogue.option', verbose_name='Options')),
            ],
            options={
                'verbose_name': 'Product class',
                'verbose_name_plural': 'Product classes',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
