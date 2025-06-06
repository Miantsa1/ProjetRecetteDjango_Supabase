# Generated by Django 4.2.15 on 2025-05-28 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produit', '0001_initial'),
        ('personne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personne.personne')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
    ]
