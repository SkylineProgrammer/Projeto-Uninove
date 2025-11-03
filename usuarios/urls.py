from django.contrib.auth import views as auth_views
from django.urls import path
from .views import CadastroUsuarioView # Mantido, mas nao estou usando na lista
from . import views 

urlpatterns = [
    # Rota raiz
    path('', views.pagina_login, name='pagina_inicial'), 

    # ROTA DE PÁGINA PRINCIPAL
    path('principal/', views.pagina_principal, name='principal'), 
    path('auth/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_page'),
    path('gamemode/', views.pagina_gamemode, name='gamemode_page'),
    path('ajuda/', views.pagina_ajuda, name='ajuda_page'),
    
    # ROTAS PREMIUM (Assinatura e Chatbot)
    path('assinar/premium/', views.assinatura_page_view, name='assinatura_page'),
    path('chatbot/', views.chatbot_page, name='chatbot_page'), 
    
    # rotas do perfil 
    path('perfil/', views.pagina_perfil, name='perfil_page'),
    path('perfil/password_change/', 
         auth_views.PasswordChangeView.as_view(
             template_name='password_change.html', 
             success_url='/perfil/password_change/done/'
         ), 
         name='password_change'),
         path('perfil/password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='password_change_done.html'
         ), 
         name='password_change_donepip install django-cors-headers'),
         # Rota para upload de imagem 
    path('perfil/upload-foto/', views.upload_foto_perfil, name='upload_foto_perfil'),


    # API para Cadastro
    path('cadastro/', views.CadastroUsuarioView.as_view(), name='cadastro_usuario_api'),
    
    # API para Login
    path('api/login-custom/', views.fazer_login, name='api_login_custom'),
    
    # ROTAS DE PÁGINAS (Frontend)
    path('registro/', views.pagina_registro, name='registro'),
]