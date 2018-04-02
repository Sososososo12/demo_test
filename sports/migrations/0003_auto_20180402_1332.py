# Generated by Django 2.1 on 2018-04-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20180322_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsAuthor',
            fields=[
                ('authorid', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('authorname', models.CharField(blank=True, max_length=100, null=True)),
                ('authoraddress', models.CharField(blank=True, max_length=50, null=True)),
                ('authoremail', models.CharField(blank=True, max_length=50, null=True)),
                ('authortel', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'sports_author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsCity',
            fields=[
                ('cityid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('cityname', models.CharField(blank=True, max_length=30, null=True)),
                ('cityprvince', models.CharField(blank=True, max_length=30, null=True)),
                ('citycountry', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'sports_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsDegree',
            fields=[
                ('degreeid', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('degreename', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'sports_degree',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsEduback',
            fields=[
                ('edubackid', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('edubackname', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'sports_eduback',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsJournal',
            fields=[
                ('journalid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('journalname', models.CharField(blank=True, max_length=20, null=True)),
                ('journalnum', models.CharField(blank=True, max_length=20, null=True)),
                ('launchdate', models.CharField(blank=True, max_length=20, null=True)),
                ('authoraddress', models.CharField(blank=True, max_length=50, null=True)),
                ('authoremail', models.CharField(blank=True, max_length=50, null=True)),
                ('authortel', models.CharField(blank=True, max_length=20, null=True)),
                ('coretype', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'sports_journal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsOrganization',
            fields=[
                ('organizationid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('orgname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'sports_organization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsOrgtype',
            fields=[
                ('orgtypeid', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('orgtypename', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'sports_orgtype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsPaper',
            fields=[
                ('paperid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('vicetitle', models.CharField(blank=True, max_length=30, null=True)),
                ('pagetype', models.CharField(blank=True, max_length=8, null=True)),
                ('publicdate', models.CharField(blank=True, max_length=20, null=True)),
                ('journalversion', models.CharField(blank=True, max_length=8, null=True)),
                ('journalpages', models.CharField(blank=True, max_length=8, null=True)),
                ('subject', models.CharField(blank=True, max_length=8, null=True)),
                ('paperauthororg', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'sports_paper',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsResearcharea',
            fields=[
                ('researchareaid', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('researchareaname', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'sports_researcharea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SportsTranslator',
            fields=[
                ('translatorid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('translatorname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'sports_translator',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='author',
            name='authorcity',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authordegree',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authoreddu',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authororg',
        ),
        migrations.RemoveField(
            model_name='author',
            name='authorresarea',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='becity',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='majordirector',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='majorhostorg',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='organtypeid',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='bejournalid',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='paperauthor',
        ),
        migrations.RemoveField(
            model_name='translator',
            name='transpaper',
        ),
        migrations.DeleteModel(
            name='author',
        ),
        migrations.DeleteModel(
            name='city',
        ),
        migrations.DeleteModel(
            name='degree',
        ),
        migrations.DeleteModel(
            name='eduback',
        ),
        migrations.DeleteModel(
            name='journal',
        ),
        migrations.DeleteModel(
            name='organization',
        ),
        migrations.DeleteModel(
            name='orgtype',
        ),
        migrations.DeleteModel(
            name='paper',
        ),
        migrations.DeleteModel(
            name='researcharea',
        ),
        migrations.DeleteModel(
            name='translator',
        ),
    ]
