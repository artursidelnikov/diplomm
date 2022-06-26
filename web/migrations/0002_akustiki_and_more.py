# Generated by Django 4.0.4 on 2022-05-09 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akustiki',
            fields=[
                ('id_veshy', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Nazvanie', models.CharField(max_length=50)),
                ('Proizvoditel', models.CharField(max_length=20)),
                ('potrebl_moshnost', models.IntegerField()),
                ('vihodnaya_moshnost', models.IntegerField()),
                ('blupup', models.CharField(max_length=20)),
                ('wifi', models.CharField(max_length=20)),
                ('Ves', models.IntegerField()),
                ('gabarit', models.CharField(max_length=14)),
                ('dinamiky', models.IntegerField()),
                ('diaazon_chastot', models.CharField(max_length=14)),
                ('iterfeysy', models.CharField(max_length=60)),
                ('oisanye', models.CharField(max_length=1000)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='kategorii_akustika',
            name='id_kategoriya_aud_tehnika',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.DeleteModel(
            name='Akustika',
        ),
        migrations.AddField(
            model_name='akustiki',
            name='id_kategoriya_aud_tehnika',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.kategorii_akustika'),
        ),
    ]
