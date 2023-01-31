# Generated by Django 4.1.5 on 2023-01-31 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='About Page Title')),
                ('details', models.TextField(verbose_name='Profile Details')),
                ('profle_photo', models.ImageField(upload_to='about_page')),
            ],
            options={
                'verbose_name_plural': '1. About',
            },
        ),
        migrations.CreateModel(
            name='CatOneCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=50, verbose_name='Card Title')),
                ('card_image', models.ImageField(upload_to='projects_page', verbose_name='Card Image')),
                ('excerpt', models.CharField(max_length=50, verbose_name='Card Exerpt')),
                ('button_one_name', models.CharField(default='Button 1', max_length=50, verbose_name='Button One')),
                ('button_two_name', models.CharField(default='Button 2', max_length=50, verbose_name='Button two')),
                ('link_1', models.TextField(default='#', verbose_name='Link one')),
                ('link_2', models.TextField(default='#', verbose_name='Link two')),
            ],
            options={
                'verbose_name': 'Category One Card',
                'verbose_name_plural': 'Category One Cards',
            },
        ),
        migrations.CreateModel(
            name='CatThreeCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=50, verbose_name='Card Title')),
                ('card_image', models.ImageField(upload_to='projects_page', verbose_name='Card Image')),
                ('excerpt', models.CharField(max_length=50, verbose_name='Card Exerpt')),
                ('button_one_name', models.CharField(default='Button 1', max_length=50, verbose_name='Button One')),
                ('button_two_name', models.CharField(default='Button 2', max_length=50, verbose_name='Button two')),
                ('link_1', models.TextField(default='#', verbose_name='Link one')),
                ('link_2', models.TextField(default='#', verbose_name='Link two')),
            ],
            options={
                'verbose_name': 'Category Three Card',
                'verbose_name_plural': 'Category Three Cards',
            },
        ),
        migrations.CreateModel(
            name='CatTwoCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=50, verbose_name='Card Title')),
                ('card_image', models.ImageField(upload_to='projects_page', verbose_name='Card Image')),
                ('excerpt', models.CharField(max_length=50, verbose_name='Card Exerpt')),
                ('button_one_name', models.CharField(default='Button 1', max_length=50, verbose_name='Button One')),
                ('button_two_name', models.CharField(default='Button 2', max_length=50, verbose_name='Button two')),
                ('link_1', models.TextField(default='#', verbose_name='Link one')),
                ('link_2', models.TextField(default='#', verbose_name='Link two')),
            ],
            options={
                'verbose_name': 'Category Two Card',
                'verbose_name_plural': 'Category Two Cards',
            },
        ),
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Certificate Title')),
                ('image', models.ImageField(upload_to='certificate_page', verbose_name='Certififcate Image')),
                ('link', models.TextField(verbose_name='Verification Link')),
            ],
            options={
                'verbose_name': 'Certificates',
                'verbose_name_plural': '3. Certificates',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('icon', models.ImageField(upload_to='contact_page', verbose_name='Icon')),
                ('dark_icon', models.ImageField(upload_to='contact_page', verbose_name='Dark_Icon')),
                ('link', models.TextField(verbose_name='Social Link')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': '4. Contacts',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Projects Page Title')),
                ('details', models.TextField(verbose_name='Projects Details')),
                ('cat_one_heading', models.CharField(max_length=50, verbose_name='Category One Heading')),
                ('cat_two_heading', models.CharField(max_length=50, verbose_name='Category Two Heading')),
                ('cat_three_heading', models.CharField(max_length=50, verbose_name='Category Three Heading')),
            ],
            options={
                'verbose_name': 'Projects',
                'verbose_name_plural': '2. Projects',
            },
        ),
        migrations.CreateModel(
            name='SiteTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='NavBar-Title')),
                ('page_title', models.CharField(max_length=50, verbose_name='Page-Title')),
            ],
            options={
                'verbose_name': 'Site Title',
                'verbose_name_plural': 'Site Title',
            },
        ),
    ]
