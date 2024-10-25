from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
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


class Maxruntime(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    changelogid = models.BigIntegerField(db_column='ChangeLogID', blank=True, null=True)   
    status = models.TextField(db_column='Status', blank=True, null=True)   
    reportdate = models.TextField(db_column='ReportDate', blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   
    metergroupid = models.BigIntegerField(db_column='MeterGroupID', blank=True, null=True)   
    opening_datetime = models.DateTimeField(db_column='Opening_DateTime', blank=True, null=True)   
    closing_datetime = models.DateTimeField(db_column='Closing_DateTime', blank=True, null=True)   
    duration = models.FloatField(db_column='Duration', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'maxruntime'


class Minruntime(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    changelogid = models.BigIntegerField(db_column='ChangeLogID', blank=True, null=True)   
    status = models.TextField(db_column='Status', blank=True, null=True)   
    reportdate = models.TextField(db_column='ReportDate', blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   
    metergroupid = models.BigIntegerField(db_column='MeterGroupID', blank=True, null=True)   
    opening_datetime = models.DateTimeField(db_column='Opening_DateTime', blank=True, null=True)   
    closing_datetime = models.DateTimeField(db_column='Closing_DateTime', blank=True, null=True)   
    duration = models.FloatField(db_column='Duration', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'minruntime'


class RuntimeDetail(models.Model):
    metergroupid = models.IntegerField(db_column='MeterGroupID', blank=True, null=True)   
    runtime = models.IntegerField(db_column='Runtime', blank=True, null=True)   
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   


    class Meta:
        managed = False
        db_table = 'runtime_detail'


class Statuschange(models.Model):
    metergroupid = models.IntegerField(db_column='MeterGroupID', blank=True, null=True)   
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)   
    changes = models.IntegerField(db_column='Changes', blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   


    class Meta:
        managed = False
        db_table = 'statuschange'


class TimeCat(models.Model):
    metergroupid = models.IntegerField(db_column='MeterGroupID', blank=True, null=True)   
    time = models.CharField(db_column='Time', max_length=20, blank=True, null=True)   
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   


    class Meta:
        managed = False
        db_table = 'time_cat'

class Purest(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    changelogid = models.BigIntegerField(db_column='ChangeLogID', blank=True, null=True)   
    status = models.TextField(db_column='Status', blank=True, null=True)   
    reportdate = models.TextField(db_column='ReportDate', blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   
    metergroupid = models.BigIntegerField(db_column='MeterGroupID', blank=True, null=True)   
    opening_datetime = models.TextField(db_column='Opening_DateTime', blank=True, null=True)   
    closing_datetime = models.TextField(db_column='Closing_DateTime', blank=True, null=True)   
    duration = models.FloatField(db_column='Duration', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'purest'

class Impurest(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    changelogid = models.BigIntegerField(db_column='ChangeLogID', blank=True, null=True)   
    status = models.TextField(db_column='Status', blank=True, null=True)   
    reportdate = models.TextField(db_column='ReportDate', blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID', blank=True, null=True)   
    metergroupid = models.BigIntegerField(db_column='MeterGroupID', blank=True, null=True)   
    opening_datetime = models.TextField(db_column='Opening_DateTime', blank=True, null=True)   
    closing_datetime = models.TextField(db_column='Closing_DateTime', blank=True, null=True)   
    duration = models.FloatField(db_column='Duration', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'impurest'

class Metermap(models.Model):
    metergroupid = models.BigIntegerField(primary_key=True,db_column='MeterGroupID')   
    metergroupname = models.CharField(db_column='MetergroupName', max_length=45, blank=True, null=True)   
    subscriberid = models.BigIntegerField(db_column='SubscriberID',null=False)   

    class Meta:
        managed = False
        db_table = 'meter_map'
