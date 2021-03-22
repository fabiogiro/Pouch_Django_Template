# Generated by Django 3.1.6 on 2021-02-11 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codecard', models.IntegerField(unique=True)),
                ('namecard', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codecomp', models.IntegerField()),
                ('namecomp', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Syndicate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codesynd', models.IntegerField(unique=True)),
                ('namesynd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codepouch', models.CharField(max_length=10)),
                ('dtarrived', models.DateField()),
                ('quant', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=11)),
                ('codecard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
                ('codecomp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
                ('codesynd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.syndicate')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='codesynd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.syndicate'),
        ),
    ]
