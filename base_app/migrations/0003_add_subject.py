# Generated by Django 4.0.2 on 2022-03-24 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_delete_subject_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_status', models.CharField(max_length=200)),
                ('Rate', models.CharField(max_length=100)),
                ('batch_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='batchsubject', to='base_app.batch')),
            ],
        ),
    ]
