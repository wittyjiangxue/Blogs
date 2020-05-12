# Generated by Django 2.1.3 on 2018-11-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='命令标题')),
                ('command', models.CharField(max_length=2000, verbose_name='命令')),
                ('describe', models.CharField(max_length=300, verbose_name='命令描述')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '命令',
                'verbose_name_plural': '命令',
            },
        ),
        migrations.CreateModel(
            name='EmailSendLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailto', models.CharField(max_length=300, verbose_name='收件人')),
                ('title', models.CharField(max_length=2000, verbose_name='邮件标题')),
                ('content', models.TextField(verbose_name='邮件内容')),
                ('send_result', models.BooleanField(default=False, verbose_name='结果')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '邮件发送log',
                'verbose_name_plural': '邮件发送log',
                'ordering': ['-created_time'],
            },
        ),
    ]
