# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbonnementReparation(models.Model):
    abbo_id = models.AutoField(db_column='ABBO_ID', blank=True, null=True)  # Field name made lowercase.
    abbo_date_debut = models.IntegerField(db_column='ABBO_DATE_DEBUT', blank=True, null=True)  # Field name made lowercase.
    abbo_date_fin = models.IntegerField(db_column='ABBO_DATE_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Abonnement_reparation'


class Client(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', blank=True, null=True)  # Field name made lowercase.
    cli_nom = models.TextField(db_column='CLI_NOM', blank=True, null=True)  # Field name made lowercase.
    cli_prenom = models.TextField(db_column='CLI_PRENOM', blank=True, null=True)  # Field name made lowercase.
    cli_adresseposte = models.TextField(db_column='CLI_ADRESSEPOSTE', blank=True, null=True)  # Field name made lowercase.
    cli_date_naissance = models.IntegerField(db_column='CLI_DATE_NAISSANCE', blank=True, null=True)  # Field name made lowercase.
    cli_mail = models.TextField(db_column='CLI_MAIL', blank=True, null=True)  # Field name made lowercase.
    cli_tel = models.IntegerField(db_column='CLI_TEl', blank=True, null=True)  # Field name made lowercase.
    cli_membre = models.IntegerField(db_column='CLI_MEMBRE', blank=True, null=True)  # Field name made lowercase.
    cli_date_debut = models.IntegerField(db_column='CLI_DATE_DEBUT', blank=True, null=True)  # Field name made lowercase.
    cli_date_fin = models.IntegerField(db_column='CLI_DATE_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'


class CommandeFournisseur(models.Model):
    commande_fourni_id = models.AutoField(db_column='COMMANDE_FOURNI_ID', blank=True, null=True)  # Field name made lowercase.
    commadne_fourni_datecommande = models.IntegerField(db_column='COMMADNE_FOURNI_DATECOMMANDE', blank=True, null=True)  # Field name made lowercase.
    commande_fourni_statut = models.TextField(db_column='COMMANDE_FOURNI_STATUT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Commande_fournisseur'


class Donateur(models.Model):
    don_id = models.AutoField(db_column='DON_ID', blank=True, null=True)  # Field name made lowercase.
    don_nom = models.TextField(db_column='DON_NOM', blank=True, null=True)  # Field name made lowercase.
    don_prenom = models.TextField(db_column='DON_PRENOM', blank=True, null=True)  # Field name made lowercase.
    don_adresseposte = models.TextField(db_column='DON_ADRESSEPOSTE', blank=True, null=True)  # Field name made lowercase.
    don_npa = models.IntegerField(db_column='DON_NPA', blank=True, null=True)  # Field name made lowercase.
    don_localite = models.TextField(db_column='DON_LOCALITE', blank=True, null=True)  # Field name made lowercase.
    don_tel = models.IntegerField(db_column='DON_TEL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Donateur'


class Facture(models.Model):
    fac_id = models.AutoField(db_column='FAC_ID', blank=True, null=True)  # Field name made lowercase.
    fac_prixnet = models.TextField(db_column='FAC_PRIXNET', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fac_date = models.IntegerField(db_column='FAC_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Facture'


class Fournisseur(models.Model):
    fourni_id = models.AutoField(db_column='FOURNI_ID', blank=True, null=True)  # Field name made lowercase.
    fourni_nom = models.TextField(db_column='FOURNI_NOM', blank=True, null=True)  # Field name made lowercase.
    fourni_adresseposte = models.TextField(db_column='FOURNI_ADRESSEPOSTE', blank=True, null=True)  # Field name made lowercase.
    fourni_tel = models.IntegerField(db_column='FOURNI_TEL', blank=True, null=True)  # Field name made lowercase.
    fourni_npa = models.IntegerField(db_column='FOURNI_NPA', blank=True, null=True)  # Field name made lowercase.
    fourni_desc = models.TextField(db_column='FOURNI_DESC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fournisseur'


class Local(models.Model):
    local_id = models.AutoField(db_column='LOCAL_ID', blank=True, null=True)  # Field name made lowercase.
    local_nom = models.TextField(db_column='LOCAL_NOM', blank=True, null=True)  # Field name made lowercase.
    local_adresseposte = models.TextField(db_column='LOCAL_ADRESSEPOSTE', blank=True, null=True)  # Field name made lowercase.
    local_npa = models.IntegerField(db_column='LOCAL_NPA', blank=True, null=True)  # Field name made lowercase.
    local_capacite = models.IntegerField(db_column='LOCAL_CAPACITE', blank=True, null=True)  # Field name made lowercase.
    local_nb_velo = models.IntegerField(db_column='LOCAL_NB_VELO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Local'


class Location(models.Model):
    loc_id = models.AutoField(db_column='LOC_ID', blank=True, null=True)  # Field name made lowercase.
    loc_statut = models.TextField(db_column='LOC_STATUT', blank=True, null=True)  # Field name made lowercase.
    loc_client_id = models.IntegerField(db_column='LOC_CLIENT_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class LocationVelo(models.Model):
    date_debut = models.IntegerField(db_column='DATE_DEBUT', blank=True, null=True)  # Field name made lowercase.
    date_fin = models.IntegerField(db_column='DATE_FIN', blank=True, null=True)  # Field name made lowercase.
    lv_loc_id = models.AutoField(db_column='LV_LOC_ID', blank=True, null=True)  # Field name made lowercase.
    lv_vel_id = models.IntegerField(db_column='LV_VEL_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location_Velo'


class MembreComite(models.Model):
    memb_id = models.AutoField(db_column='MEMB_ID', blank=True, null=True)  # Field name made lowercase.
    memb_nom = models.IntegerField(db_column='MEMB_NOM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Membre_Comite'


class Parametre(models.Model):
    caution = models.IntegerField(db_column='CAUTION', blank=True, null=True)  # Field name made lowercase.
    prixmin = models.IntegerField(db_column='PRIXMIN', blank=True, null=True)  # Field name made lowercase.
    prixmois = models.IntegerField(db_column='PRIXMOIS', blank=True, null=True)  # Field name made lowercase.
    prixabbo = models.IntegerField(db_column='PRIXABBO', blank=True, null=True)  # Field name made lowercase.
    locationmoismin = models.IntegerField(db_column='LOCATIONMOISMIN', blank=True, null=True)  # Field name made lowercase.
    locationmoismax = models.IntegerField(db_column='LOCATIONMOISMAX', blank=True, null=True)  # Field name made lowercase.
    a_propos = models.TextField(db_column='A_PROPOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parametre'


class PieceCommandeFourni(models.Model):
    quantite_commande = models.IntegerField(db_column='QUANTITE_COMMANDE', blank=True, null=True)  # Field name made lowercase.
    pcf_piece_id = models.AutoField(db_column='PCF_PIECE_ID', blank=True, null=True)  # Field name made lowercase.
    pcf_commande_fourni_id = models.IntegerField(db_column='PCF_COMMANDE_FOURNI_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Piece_Commande_fourni'


class PieceDeVelo(models.Model):
    piece_id = models.AutoField(db_column='PIECE_ID', blank=True, null=True)  # Field name made lowercase.
    piece_type = models.TextField(db_column='PIECE_TYPE', blank=True, null=True)  # Field name made lowercase.
    piece_num = models.IntegerField(db_column='PIECE_NUM', blank=True, null=True)  # Field name made lowercase.
    piece_marque = models.TextField(db_column='PIECE_MARQUE', blank=True, null=True)  # Field name made lowercase.
    piece_nb = models.IntegerField(db_column='PIECE_NB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Piece_de_velo'


class Velo(models.Model):
    vel_id = models.AutoField(db_column='VEL_ID', blank=True, null=True)  # Field name made lowercase.
    vel_num_cadre = models.IntegerField(db_column='VEL_NUM_CADRE', blank=True, null=True)  # Field name made lowercase.
    vel_nom = models.TextField(db_column='VEL_NOM', blank=True, null=True)  # Field name made lowercase.
    vel_marque = models.TextField(db_column='VEL_MARQUE', blank=True, null=True)  # Field name made lowercase.
    vel_couleur = models.TextField(db_column='VEL_COULEUR', blank=True, null=True)  # Field name made lowercase.
    vel_type = models.TextField(db_column='VEL_TYPE', blank=True, null=True)  # Field name made lowercase.
    vel_photo = models.TextField(db_column='VEL_PHOTO', blank=True, null=True)  # Field name made lowercase.
    vel_statut = models.TextField(db_column='VEL_STATUT', blank=True, null=True)  # Field name made lowercase.
    vel_etat = models.TextField(db_column='VEL_ETAT', blank=True, null=True)  # Field name made lowercase.
    vel_remarque = models.TextField(db_column='VEL_REMARQUE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Velo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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
