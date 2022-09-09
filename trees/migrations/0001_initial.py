# Generated by Django 4.1.1 on 2022-09-07 19:43

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Família',
                'verbose_name_plural': 'Famílias',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Espécie',
                'verbose_name_plural': 'Espécies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nome')),
                ('is_display', models.BooleanField(default=True, verbose_name='Exibir')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Endereço')),
                ('image1', models.CharField(blank=True, max_length=150, verbose_name='nome imagem 1')),
                ('altimg1', models.CharField(blank=True, max_length=150, verbose_name='Alt imagem 1')),
                ('image2', models.CharField(blank=True, max_length=150, verbose_name='nome imagem 2')),
                ('altimg2', models.CharField(blank=True, max_length=150, verbose_name='Alt imagem 2')),
                ('image3', models.CharField(blank=True, max_length=150, verbose_name='nome imagem 3')),
                ('altimg3', models.CharField(blank=True, max_length=150, verbose_name='Alt imagem 3')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Praça',
                'verbose_name_plural': 'Praças',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Nome popular')),
                ('source', models.CharField(choices=[('nativa', 'Nativa'), ('exótica', 'Exótica'), ('nativa e exótica', 'Nativa e Exótica')], max_length=20, verbose_name='Origem')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('is_display', models.BooleanField(default=True, verbose_name='Exibir')),
                ('image1', models.CharField(blank=True, max_length=150, verbose_name='nome imagem 1')),
                ('altimg1', models.CharField(blank=True, max_length=150, verbose_name='Alt imagem 1')),
                ('image2', models.CharField(blank=True, max_length=150, verbose_name='nome imagem 2')),
                ('altimg2', models.CharField(blank=True, max_length=150, verbose_name='Alt imagem 2')),
                ('image3', models.CharField(blank=True, max_length=150, verbose_name='nome imagem 3')),
                ('altimg3', models.CharField(blank=True, max_length=150, verbose_name='Alt imagem 3')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family', to='trees.family')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species', to='trees.specie')),
                ('square', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees', to='trees.square')),
            ],
            options={
                'verbose_name': 'Árvore',
                'verbose_name_plural': 'Árvores',
                'ordering': ('name',),
            },
        ),
    ]
