# Generated by Django 3.2.4 on 2021-07-29 06:58

import client.models
import datetime
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_client', models.BooleanField(default=False)),
                ('is_worker', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestedService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('workload', models.IntegerField(default=0, verbose_name='Workload')),
                ('timing', models.IntegerField(default=0, verbose_name='Number of days')),
                ('address', models.CharField(default='', max_length=255, verbose_name='Address')),
                ('budget', models.IntegerField(default=0, verbose_name='Budget')),
                ('created_on', models.DateTimeField(default=datetime.datetime(2021, 7, 29, 6, 58, 41, 94055, tzinfo=utc), verbose_name='Created on')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_num', models.IntegerField(null=True)),
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerPortfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Name of the work')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.worker')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.categories')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_price', to='client.worker')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerPortfolioPhoto',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_name', models.CharField(default='default', max_length=20)),
                ('image_url', models.ImageField(default='default.jpg', upload_to=client.models.upload_works, verbose_name='Image')),
                ('workerPortfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.workerportfolio')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('response_detail', models.CharField(max_length=300, verbose_name='Details')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.requestedservice')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.worker')),
            ],
        ),
        migrations.CreateModel(
            name='RequestPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(default='default', max_length=20)),
                ('image_url', models.ImageField(default='default2.jpg', upload_to=client.models.upload_schemas, verbose_name='Image')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.requestedservice')),
            ],
        ),
        migrations.AddField(
            model_name='requestedservice',
            name='sub_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='client.subcategories'),
        ),
        migrations.AddField(
            model_name='requestedservice',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.worker'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True, verbose_name='comment')),
                ('rate', models.IntegerField(verbose_name='rate')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client', verbose_name='client')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.worker', verbose_name='worker')),
            ],
        ),
    ]