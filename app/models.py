
from django.db import models


class Banco(models.Model):
    idbanco = models.IntegerField(primary_key=True)
    nombreclib = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    apellidoclib = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    telefonoclib = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    emailclib = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    direclib = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    hipoteca = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BANCO'


class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombrecli = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    apellidocli = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    telefonocli = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    emailcli = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    direcli = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    servicio = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.idcliente:  # Verificar si no se ha asignado un ID
            last_id = Cliente.objects.order_by('-idcliente').first()
            self.idcliente = 1 if last_id is None else last_id.idcliente + 1
        super(LogHistorialcliente, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'CLIENTE'


class Eqinsp(models.Model):
    idequipo = models.IntegerField()
    nombres = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    estadoequipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EQINSP'


class Inspeccion(models.Model):
    idinspeccion = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=250, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    idusuario = models.IntegerField(blank=True, null=True)
    idequipo = models.IntegerField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    fechains = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'INSPECCION'


class LogHistorialcliente(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_HISTORIALCLIENTE'


class LogHistorialeqinsp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        managed = False
        db_table = 'LOG_HISTORIALEQINSP'


class Salida(models.Model):
    idsalida = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idequipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SALIDA'


class Solicitud(models.Model):

    OPCIONES = (
    ('1', 'Reparacion'),
    ('2', 'Remodelacion'),
    ('3', 'Otros'),
)
    id_solicitud = models.IntegerField(primary_key=True)
    run_cli = models.CharField(max_length=12, db_collation='Modern_Spanish_CI_AS')
    run_emp = models.CharField(max_length=12, db_collation='Modern_Spanish_CI_AS')
    tipo_solicitud = models.CharField(max_length=12,blank=True, null=True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.id_solicitud:  # Verificar si no se ha asignado un ID
            last_id = Solicitud.objects.order_by('-id_solicitud').first()
            self.id_solicitud = 1 if last_id is None else last_id.id_solicitud + 1
        super(Solicitud, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'SOLICITUD'

        


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50, db_collation='Modern_Spanish_CI_AS')
    active = models.BooleanField()
    title = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS')
    title_visible = models.BooleanField()
    logo = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    logo_visible = models.BooleanField()
    css_header_background_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    title_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_header_text_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_header_link_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_header_link_hover_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_module_background_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_module_text_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_module_link_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_module_link_hover_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_module_rounded_corners = models.BooleanField()
    css_generic_link_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_generic_link_hover_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_save_button_background_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_save_button_background_hover_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_save_button_text_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_delete_button_background_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_delete_button_background_hover_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_delete_button_text_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    list_filter_dropdown = models.BooleanField()
    related_modal_active = models.BooleanField()
    related_modal_background_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    related_modal_rounded_corners = models.BooleanField()
    logo_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    recent_actions_visible = models.BooleanField()
    favicon = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    related_modal_background_opacity = models.CharField(max_length=5, db_collation='Modern_Spanish_CI_AS')
    env_name = models.CharField(max_length=50, db_collation='Modern_Spanish_CI_AS')
    env_visible_in_header = models.BooleanField()
    env_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    env_visible_in_favicon = models.BooleanField()
    related_modal_close_button_visible = models.BooleanField()
    language_chooser_active = models.BooleanField()
    language_chooser_display = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    list_filter_sticky = models.BooleanField()
    form_pagination_sticky = models.BooleanField()
    form_submit_sticky = models.BooleanField()
    css_module_background_selected_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    css_module_link_selected_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    logo_max_height = models.SmallIntegerField()
    logo_max_width = models.SmallIntegerField()
    foldable_apps = models.BooleanField()
    language_chooser_control = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS')
    list_filter_highlight = models.BooleanField()
    list_filter_removal_links = models.BooleanField()
    show_fieldsets_as_tabs = models.BooleanField()
    show_inlines_as_tabs = models.BooleanField()
    css_generic_link_active_color = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

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
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    object_id = models.TextField(db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Modern_Spanish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Modern_Spanish_CI_AS')
    session_data = models.TextField(db_collation='Modern_Spanish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
