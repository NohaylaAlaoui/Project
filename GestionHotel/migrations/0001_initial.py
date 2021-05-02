# Generated by Django 3.1.4 on 2021-05-02 02:23

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chamber_number', models.IntegerField()),
                ('chamber_stage', models.IntegerField()),
                ('chamber_phone', phone_field.models.PhoneField(blank=True, help_text='numero de telephone de la chambre', max_length=31)),
                ('chamber_reserved', models.BooleanField()),
                ('chamber_cleaned', models.BooleanField()),
            ],
            options={
                'ordering': ['chamber_stage', 'chamber_number'],
            },
        ),
        migrations.CreateModel(
            name='ChamberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=60)),
                ('type_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ['type_name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='numero de telephone', max_length=31)),
                ('email_client', models.EmailField(blank=True, max_length=254, null=True)),
                ('identificator_type', models.CharField(choices=[('PS', 'Passport'), ('IC', 'Identity Card')], max_length=2)),
                ('id_number', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='numero de telephone', max_length=31)),
                ('email_client', models.EmailField(blank=True, max_length=254, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_reservation', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('chambre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.chamber')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.client')),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='OnlineRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone_number', phone_field.models.PhoneField(help_text='numero de telephone', max_length=31)),
                ('email_client', models.EmailField(blank=True, max_length=254, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ChamberType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.chambertype')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('nw', 'new'), ('sent', 'sent'), ('retu', 'returned'), ('paid', 'paid'), ('cred', 'credited'), ('inco', 'uncollectible')], default='nw', max_length=4)),
                ('note', models.CharField(blank=True, default='Thank you for using our services', max_length=60)),
                ('date_due', models.DateField(help_text='date de payment')),
                ('date_sent', model_utils.fields.MonitorField(blank=True, default=None, monitor='status', verbose_name="date d'envoi", when={'sent'})),
                ('date_paid', model_utils.fields.MonitorField(blank=True, default=None, monitor='status', verbose_name='date de paiement', when={'paid'})),
                ('payment_method', models.CharField(choices=[('pick', 'personal pick up'), ('emal', 'mailing'), ('dig', 'digital')], max_length=4)),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.reservation')),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.AddField(
            model_name='chamber',
            name='chamber_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionHotel.chambertype'),
        ),
    ]
