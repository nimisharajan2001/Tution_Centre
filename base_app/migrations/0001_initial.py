# Generated by Django 4.0.2 on 2022-03-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('batch_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='batchdesignation', to='base_app.batch')),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('fathername', models.CharField(max_length=240, null=True)),
                ('mothername', models.CharField(max_length=240, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=240, null=True)),
                ('presentaddress1', models.CharField(max_length=240, null=True)),
                ('presentaddress2', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('district', models.CharField(max_length=240, null=True)),
                ('state', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('permanentaddress1', models.CharField(max_length=240, null=True)),
                ('permanentaddress2', models.CharField(max_length=240, null=True)),
                ('permanentpincode', models.CharField(max_length=240, null=True)),
                ('permanentdistrict', models.CharField(max_length=240, null=True)),
                ('permanentstate', models.CharField(max_length=240, null=True)),
                ('permanentcountry', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('alternativeno', models.CharField(max_length=240, null=True)),
                ('employee_id', models.CharField(default='', max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
                ('idproof', models.FileField(blank=True, null=True, upload_to='images/')),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('joiningdate', models.DateField(blank=True, null=True)),
                ('total_pay', models.IntegerField(default='0')),
                ('payment_balance', models.IntegerField(default='0')),
                ('account_no', models.CharField(default='', max_length=200, null=True)),
                ('ifsc', models.CharField(default='', max_length=200, null=True)),
                ('bank_name', models.CharField(default='', max_length=240, null=True)),
                ('bank_branch', models.CharField(default='', max_length=240, null=True)),
                ('payment_status', models.CharField(default='', max_length=200, null=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationbatch', to='base_app.batch')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationdesignation', to='base_app.designation')),
            ],
        ),
        migrations.CreateModel(
            name='subject_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_name', models.CharField(max_length=100)),
                ('Subject_status', models.CharField(max_length=200)),
                ('Rate', models.CharField(max_length=100)),
                ('batch_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='batchsubject', to='base_app.batch')),
            ],
        ),
        migrations.CreateModel(
            name='reported_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('reported_date', models.DateField(blank=True, null=True)),
                ('reply', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('issuestatus', models.CharField(max_length=200)),
                ('designation_id', models.CharField(max_length=200)),
                ('reported_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereported_to', to='base_app.user_registration')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereporter', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='class_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('batch_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='batchclass', to='base_app.batch')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=200)),
                ('attendance_status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendanceuser', to='base_app.user_registration')),
            ],
        ),
    ]