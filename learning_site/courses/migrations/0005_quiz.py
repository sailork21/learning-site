# Generated by Django 2.2 on 2019-04-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190425_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('total_questions', models.IntegerField(default=4)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Course')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
    ]