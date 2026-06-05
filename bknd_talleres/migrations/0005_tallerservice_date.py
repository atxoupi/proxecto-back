from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bknd_talleres', '0004_alter_tallerservice_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tallerservice',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
