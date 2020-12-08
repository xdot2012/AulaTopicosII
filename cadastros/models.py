from django.db import models
from django.contrib.auth.models import PermissionsMixin, Permission, Group
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager



class UsuarioManager(BaseUserManager):
    def create_user(self, login, nome, email, password=None):

        user = self.model(
            login=login,
            nome=nome,
            email=email

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, nome, email, password):

        user = self.create_user(
            login,
            nome,
            email

        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class Usuario(AbstractBaseUser, PermissionsMixin):
    """Model definition for Usuario."""

    nome = models.CharField('Nome', max_length=80)
    login = models.CharField('Login', max_length=50, unique=True)
    password = models.CharField('Senha', max_length=128)
    email = models.EmailField('Email', max_length=254)

    # campos necessários pra o DJango
    last_login = models.DateTimeField(
        'Último login', blank=True, null=True, db_column='last_login')
    is_active = models.BooleanField('Ativo', default=True)
    is_admin = models.BooleanField('Ativo', default=False)
    is_staff = models.BooleanField('Staff', default=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True)

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nome','email']

    objects = UsuarioManager()


    def get_full_name(self):
        return self.Nome
    
   
    class Meta:
        """Meta definition for Usuario."""

        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        """Unicode representation of Usuario."""
        return self.Nome



# Create your models here.
PROFISSAO = (
        ('ENGENHEIRO', 'Engenheiro'),
        ('PROFESSOR', 'Professor'),
        ('ESTUDANTE', 'Estudante'),
    )



class Pessoa(models.Model):

    nome = models.CharField('Nome da Pessoa',max_length=150, null=True, blank=True )
    profissao = models.CharField('Profissão',max_length=150, choices=PROFISSAO, null=True)
    endereco = models.CharField('Endereço',max_length=150, null=True, blank=True)
    numero = models.IntegerField('Numero', null=True, blank=True)

    date = models.DateField('Data',null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.nome}'+' - '+f'{self.numero}'
    