# Generated by Django 2.2 on 2019-04-25 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_quiz'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('prompt', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Quiz')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
