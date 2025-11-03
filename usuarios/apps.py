from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios' 

    def ready(self):
        # Importar o arquivo signals para que o Django o reconheça
        import usuarios.signals 
