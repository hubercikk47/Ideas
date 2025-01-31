# Generated by Django 3.2.25 on 2025-01-30 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0004_alter_idea_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='idea',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('review', 'Under Review'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=15),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.idea')),
            ],
        ),
    ]
