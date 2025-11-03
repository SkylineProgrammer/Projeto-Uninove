from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil # Importa Perfil de models.py

@receiver(post_save, sender=User)
def criar_ou_atualizar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Cria automaticamente o Perfil quando um novo User é criado.
    Salva o Perfil quando o User é atualizado.
    """
    # Cria o perfil se o usuario for novo 
    if created:
        Perfil.objects.create(user=instance, is_assinante=False)
    
    # Salva o perfil sempre que o User for salvo
    # Usando para lidar com o erro de usuarios antigos sem perfil
    try:
        instance.perfil.save()
    except Perfil.DoesNotExist:
        Perfil.objects.create(user=instance, is_assinante=False)