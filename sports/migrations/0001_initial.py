# Generated by Django 2.1 on 2018-03-20 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('authorid', models.CharField(max_length=17, primary_key=True, serialize=False, verbose_name='作者id')),
                ('authorname', models.CharField(max_length=20, null=True, verbose_name='作者名称')),
                ('authoraddress', models.CharField(max_length=50, null=True, verbose_name='通讯地址')),
                ('authoremail', models.CharField(max_length=50, null=True, verbose_name='EMAIL')),
                ('authortel', models.CharField(max_length=20, null=True, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '作者信息',
                'verbose_name_plural': '作者信息',
            },
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('cityid', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='城市代码')),
                ('cityname', models.CharField(max_length=30, null=True, verbose_name='城市名称')),
                ('cityprvince', models.CharField(max_length=30, null=True, verbose_name='省份名称')),
                ('citycountry', models.CharField(max_length=30, null=True, verbose_name='国家名称')),
            ],
            options={
                'verbose_name': '城市信息',
                'verbose_name_plural': '城市信息',
            },
        ),
        migrations.CreateModel(
            name='degree',
            fields=[
                ('degreeid', models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='学位代码')),
                ('degreename', models.CharField(max_length=10, null=True, verbose_name='学位名称')),
            ],
            options={
                'verbose_name': '学位信息',
                'verbose_name_plural': '学位信息',
            },
        ),
        migrations.CreateModel(
            name='eduback',
            fields=[
                ('edubackid', models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='学历代码')),
                ('edubackname', models.CharField(max_length=10, null=True, verbose_name='学历名称')),
            ],
            options={
                'verbose_name': '学历信息',
                'verbose_name_plural': '学历信息',
            },
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('journalid', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='期刊代码')),
                ('journalname', models.CharField(max_length=20, null=True, verbose_name='标题')),
                ('journalnum', models.CharField(max_length=20, null=True, verbose_name='刊号')),
                ('launchdate', models.CharField(max_length=20, null=True, verbose_name='创刊时间')),
                ('authoraddress', models.CharField(max_length=50, null=True, verbose_name='通讯地址')),
                ('authoremail', models.CharField(max_length=50, null=True, verbose_name='EMAIL')),
                ('authortel', models.CharField(max_length=20, null=True, verbose_name='联系电话')),
                ('coretype', models.CharField(max_length=1, null=True, verbose_name='核心期刊类型')),
                ('becity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.city')),
                ('majordirector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.author')),
            ],
            options={
                'verbose_name': '期刊信息',
                'verbose_name_plural': '期刊信息',
            },
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('organizationid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='机构代码')),
                ('orgname', models.CharField(max_length=30, verbose_name='机构名称')),
            ],
            options={
                'verbose_name': '机构信息',
                'verbose_name_plural': '机构信息',
            },
        ),
        migrations.CreateModel(
            name='orgtype',
            fields=[
                ('orgtypeid', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='机构类别代码')),
                ('orgtypename', models.CharField(max_length=30, null=True, verbose_name='机构类别名称')),
            ],
            options={
                'verbose_name': '研究方向信息',
                'verbose_name_plural': '研究方向信息',
            },
        ),
        migrations.CreateModel(
            name='paper',
            fields=[
                ('paperid', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='文献代码')),
                ('title', models.CharField(max_length=30, null=True, verbose_name='文献标题')),
                ('vicetitle', models.CharField(max_length=30, null=True, verbose_name='文献副标题')),
                ('pagetype', models.CharField(max_length=8, null=True, verbose_name='版类')),
                ('publicdate', models.CharField(max_length=20, null=True, verbose_name='年份')),
                ('journalversion', models.CharField(max_length=8, null=True, verbose_name='源刊期号')),
                ('journalpages', models.CharField(max_length=8, null=True, verbose_name='源刊页号')),
                ('subject', models.CharField(max_length=8, null=True, verbose_name='学科')),
                ('bejournalid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.journal')),
                ('paperauthor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.author')),
                ('paperauthororg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.organization')),
            ],
            options={
                'verbose_name': '文献信息',
                'verbose_name_plural': '文献信息',
            },
        ),
        migrations.CreateModel(
            name='researcharea',
            fields=[
                ('researchareaid', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='研究方向代码')),
                ('researchareaname', models.CharField(max_length=30, null=True, verbose_name='研究方向名称')),
            ],
            options={
                'verbose_name': '研究方向信息',
                'verbose_name_plural': '研究方向信息',
            },
        ),
        migrations.CreateModel(
            name='translator',
            fields=[
                ('translatorid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='机构代码')),
                ('translatorname', models.CharField(max_length=30, verbose_name='译者名称')),
                ('transpaper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.paper')),
            ],
            options={
                'verbose_name': '译者信息',
                'verbose_name_plural': '译者信息',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='organtypeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.orgtype'),
        ),
        migrations.AddField(
            model_name='journal',
            name='majorhostorg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.organization'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorcity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.city'),
        ),
        migrations.AddField(
            model_name='author',
            name='authordegree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.degree'),
        ),
        migrations.AddField(
            model_name='author',
            name='authoreddu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.eduback'),
        ),
        migrations.AddField(
            model_name='author',
            name='authororg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.organization'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorresarea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.researcharea'),
        ),
    ]
