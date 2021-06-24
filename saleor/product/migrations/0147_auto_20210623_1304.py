# Generated by Django 3.2.4 on 2021-06-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0146_auto_20210518_0945"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="is_preorder",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="preorder_end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="preorder_global_threshold",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="productvariantchannellisting",
            name="preorder_quantity_threshold",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
