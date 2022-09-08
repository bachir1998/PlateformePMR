# Generated by Django 3.2.3 on 2022-09-08 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('pmr', 'locataire'), ('bailleur', 'loueur'), ('admin', 'administrateur')], max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bailleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('number', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('full_adress', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('siret', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('type_user', models.CharField(choices=[('pmr', 'locataire'), ('bailleur', 'loueur')], default='pmr', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_id', models.IntegerField()),
                ('pmr_id', models.IntegerField()),
                ('date_cand', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pmr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('number', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('full_adress', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('school_proof', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('university', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pmr_proof', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('type_user', models.CharField(choices=[('pmr', 'locataire'), ('bailleur', 'loueur')], default='bailleur', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residence_name', models.CharField(max_length=100)),
                ('area', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('adress', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('zip_code', models.IntegerField(blank=True, default=None, null=True)),
                ('desc', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('date_pub', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disponible', 'disponible'), ('candidature', 'candidature'), ('archive', 'archive')], default=('disponible', 'disponible'), max_length=50)),
                ('bailleur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bailleur')),
            ],
        ),
    ]
