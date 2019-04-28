# Generated by Django 2.2 on 2019-04-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Digite a língua nativa do livro', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Manutenção'), ('e', 'Emprestado'), ('d', 'Disponível'), ('r', 'Reservado')], default='m', help_text='Disponibilidade do livro', max_length=1),
        ),
    ]
