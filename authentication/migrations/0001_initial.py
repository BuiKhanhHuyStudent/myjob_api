# Generated by Django 4.1.6 on 2023-05-26 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True)),
                ('avatar_url', models.URLField(default='https://res.cloudinary.com/dtnpj540t/image/upload/v1680687265/my-job/images_default/avt_default.jpg', max_length=300)),
                ('avatar_public_id', models.CharField(max_length=300, null=True)),
                ('email_notification_active', models.BooleanField(default=True)),
                ('sms_notification_active', models.BooleanField(default=True)),
                ('has_company', models.BooleanField(default=False)),
                ('is_verify_email', models.BooleanField(default=False)),
                ('role_name', models.CharField(choices=[('ADMIN', 'Quản trị viên'), ('EMPLOYER', 'Nhà tuyển dụng'), ('JOB_SEEKER', 'Người tìm việc')], default='JOB_SEEKER', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'myjob_authentication_user',
            },
        ),
        migrations.CreateModel(
            name='ForgotPasswordToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=255, null=True)),
                ('code', models.IntegerField(null=True)),
                ('expired_at', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('platform', models.CharField(choices=[('WEB', 'Website'), ('APP', 'Ứng dụng')], default='WEB', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forgot_password_tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'myjob_authentication_forgot_password_token',
            },
        ),
    ]
