# Generated by Django 2.2 on 2023-03-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0004_auto_20230317_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='item_image',
            field=models.CharField(default='https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2021/08/how-to-make-an-online-portfolio.png', max_length=500),
        ),
    ]
