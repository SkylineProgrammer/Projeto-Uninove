from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)
#  IMPORTAÇÃO para usuarios/ autentificaçoes
from django.contrib.auth import views as auth_views 
from usuarios import views as user_views


# Importaçoes de arquivos estaticos e de midia
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # 1 ADMIN
    path('admin/', admin.site.urls),


    # APLICATIVOS DO 'USUARIOS'
    path('', include('usuarios.urls')), 
    path('',user_views.pagina_login, name='pagina_inicial'),

    #rota para pagina principal
    path('', include('quiz.urls')),
    

    # 3 AUTENTICAÇÃO JWT (API)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
   # 4 ROTAS DE AUTENTIFICAÇAO
    
    path('auth/login/', auth_views.LoginView.as_view(template_name='login.html'), name='auth_login_page'),
      
    
    # 5 ROTAS NATIVAS PARA RECUPERAÇÃO DE SENHA 
    
    path('auth/', include('django.contrib.auth.urls')),
]


# ARQUIVOS DE MiDIA
if settings.DEBUG:
    # (CSS, JS) a partir do STATIC_URL. Mudei para STATIC_ROOT por convenção
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # (uploads)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)