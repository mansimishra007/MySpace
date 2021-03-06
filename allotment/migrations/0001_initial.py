# Generated by Django 2.2 on 2021-04-09 05:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_warden', models.BooleanField(default=False)),
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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=100)),
                ('year', models.CharField(max_length=10)),
                ('room_type', models.CharField(choices=[('SGL', 'Single Occupancy'), ('DLB', 'Double Occupancy'), ('TLB', 'Triple Occupancy')], default='TLB', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('hostel_name', models.CharField(max_length=20)),
                ('warden_assigned', models.CharField(blank=True, max_length=100)),
                ('total_no_floors', models.IntegerField()),
                ('total_no_rooms', models.IntegerField()),
                ('vacant_beds', models.IntegerField()),
                ('course', models.ManyToManyField(blank=True, default=None, to='allotment.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=5)),
                ('room_name', models.CharField(max_length=10)),
                ('room_type', models.CharField(choices=[('SGL', 'Single Occupancy'), ('DLB', 'Double Occupancy'), ('TLB', 'Triple Occupancy')], default='TLB', max_length=3)),
                ('vacant', models.BooleanField(default=False)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.Hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_first_name', models.CharField(max_length=200, null=True)),
                ('student_last_name', models.CharField(max_length=200, null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('mother_name', models.CharField(max_length=200, null=True)),
                ('smart_card_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
                ('dob', models.DateField(help_text='format : YYYY-MM-DD', max_length=10, null=True)),
                ('room_allotted', models.BooleanField(default=False)),
                ('no_dues', models.BooleanField(default=True)),
                ('course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='allotment.Course')),
                ('room', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allotment.Room')),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
