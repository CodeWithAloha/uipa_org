# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foirequest', '0003_foirequest_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='foirequest',
            name='is_blocked',
            field=models.BooleanField(default=False, verbose_name='Blocked'),
        ),
    ]
