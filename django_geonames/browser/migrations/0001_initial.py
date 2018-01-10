from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('country_code', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
    ]
