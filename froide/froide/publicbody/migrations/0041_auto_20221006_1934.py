# Generated by Django 4.0.7 on 2022-10-06 17:34

from datetime import datetime

from django.db import migrations


def convert_change_proposals(apps, schema_editor):
    PublicBody = apps.get_model("publicbody", "PublicBody")
    PublicBodyChangeProposal = apps.get_model("publicbody", "PublicBodyChangeProposal")
    for publicbody in PublicBody.objects.exclude(change_proposals={}):
        for user_id, proposal in publicbody.change_proposals.items():
            data = proposal["data"]
            timestamp = datetime.fromisoformat(proposal["timestamp"])
            # detect foreign key fields
            new_data = {}
            for key, value in data.items():
                if hasattr(PublicBody._meta.get_field(key), "remote_field"):
                    new_data[key + "_id"] = value
                else:
                    new_data[key] = value
            PublicBodyChangeProposal.objects.create(
                publicbody=publicbody, user_id=user_id, created_at=timestamp, **new_data
            )


class Migration(migrations.Migration):
    dependencies = [
        ("publicbody", "0040_alter_foilaw_options_alter_category_slug_and_more"),
    ]

    operations = [
        migrations.RunPython(convert_change_proposals),
    ]