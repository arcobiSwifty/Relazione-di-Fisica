# Generated by Django 2.1 on 2018-11-17 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisica', '0004_auto_20181117_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esperimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('es1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es1', to='fisica.Misurazione')),
                ('es10', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es10', to='fisica.Misurazione')),
                ('es11', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es11', to='fisica.Misurazione')),
                ('es12', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es12', to='fisica.Misurazione')),
                ('es2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es2', to='fisica.Misurazione')),
                ('es3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es3', to='fisica.Misurazione')),
                ('es4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es4', to='fisica.Misurazione')),
                ('es5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es5', to='fisica.Misurazione')),
                ('es6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es6', to='fisica.Misurazione')),
                ('es7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es7', to='fisica.Misurazione')),
                ('es8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es8', to='fisica.Misurazione')),
                ('es9', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es9', to='fisica.Misurazione')),
            ],
        ),
    ]