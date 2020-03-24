# Generated by Finn Stutzenstein on 2019-07-23 13:37

from django.db import migrations

from openslides.users.db import postgres_restart_auth_group_id_sequence


class Migration(migrations.Migration):
    """
    When migrating old databases (especially after 0007_superadmin) the id sequence
    in postgres needs to be restarted.

    This is a additional migration to 0007_superadmin. If a later migration does
    something with changing groups in the database, this method needs to run again.
    """

    dependencies = [("users", "0010_auto_20190119_1447")]

    operations = [migrations.RunPython(postgres_restart_auth_group_id_sequence)]