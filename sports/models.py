# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SportsAuthor(models.Model):
    authorid = models.CharField(primary_key=True, max_length=17)
    authorname = models.CharField(max_length=100, blank=True, null=True)
    authoraddress = models.CharField(max_length=50, blank=True, null=True)
    authoremail = models.CharField(max_length=50, blank=True, null=True)
    authortel = models.CharField(max_length=20, blank=True, null=True)
    authorcity = models.ForeignKey('SportsCity', models.DO_NOTHING, blank=True, null=True)
    authordegree = models.ForeignKey('SportsDegree', models.DO_NOTHING, blank=True, null=True)
    authoreddu = models.ForeignKey('SportsEduback', models.DO_NOTHING, blank=True, null=True)
    authororg = models.ForeignKey('SportsOrganization', models.DO_NOTHING, blank=True, null=True)
    authorresarea = models.ForeignKey('SportsResearcharea', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_author'


class SportsCity(models.Model):
    cityid = models.CharField(primary_key=True, max_length=6)
    cityname = models.CharField(max_length=30, blank=True, null=True)
    cityprvince = models.CharField(max_length=30, blank=True, null=True)
    citycountry = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_city'


class SportsDegree(models.Model):
    degreeid = models.CharField(primary_key=True, max_length=1)
    degreename = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_degree'


class SportsEduback(models.Model):
    edubackid = models.CharField(primary_key=True, max_length=1)
    edubackname = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_eduback'


class SportsJournal(models.Model):
    journalid = models.CharField(primary_key=True, max_length=8)
    journalname = models.CharField(max_length=20, blank=True, null=True)
    journalnum = models.CharField(max_length=20, blank=True, null=True)
    launchdate = models.CharField(max_length=20, blank=True, null=True)
    authoraddress = models.CharField(max_length=50, blank=True, null=True)
    authoremail = models.CharField(max_length=50, blank=True, null=True)
    authortel = models.CharField(max_length=20, blank=True, null=True)
    coretype = models.CharField(max_length=1, blank=True, null=True)
    becity = models.ForeignKey(SportsCity, models.DO_NOTHING, blank=True, null=True)
    majordirector = models.ForeignKey(SportsAuthor, models.DO_NOTHING, blank=True, null=True)
    majorhostorg = models.ForeignKey('SportsOrganization', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_journal'


class SportsOrganization(models.Model):
    organizationid = models.CharField(primary_key=True, max_length=10)
    orgname = models.CharField(max_length=30)
    organtypeid = models.ForeignKey('SportsOrgtype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_organization'


class SportsOrgtype(models.Model):
    orgtypeid = models.CharField(primary_key=True, max_length=2)
    orgtypename = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_orgtype'


class SportsPaper(models.Model):
    paperid = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=100, blank=True, null=True)
    vicetitle = models.CharField(max_length=30, blank=True, null=True)
    pagetype = models.CharField(max_length=8, blank=True, null=True)
    publicdate = models.CharField(max_length=20, blank=True, null=True)
    journalversion = models.CharField(max_length=8, blank=True, null=True)
    journalpages = models.CharField(max_length=8, blank=True, null=True)
    subject = models.CharField(max_length=8, blank=True, null=True)
    bejournalid = models.ForeignKey(SportsJournal, models.DO_NOTHING, blank=True, null=True)
    paperauthor = models.ForeignKey(SportsAuthor, models.DO_NOTHING, blank=True, null=True)
    paperauthororg = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_paper'


class SportsResearcharea(models.Model):
    researchareaid = models.CharField(primary_key=True, max_length=9)
    researchareaname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_researcharea'


class SportsTranslator(models.Model):
    translatorid = models.CharField(primary_key=True, max_length=10)
    translatorname = models.CharField(max_length=30)
    transpaper = models.ForeignKey(SportsPaper, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sports_translator'
