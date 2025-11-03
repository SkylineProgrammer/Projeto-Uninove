from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Django REST Framework importaçoes que fiz
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import PerfilFotoForm
# Import para cadastro
from .serializers import CadastroUsuarioSerializer


# Views de Templates

def pagina_login(request):
    """Renderiza a página de login."""
    return render(request, 'login.html') 

def pagina_registro(request):
    """Renderiza a página de registro."""
    return render(request, 'registro.html') 

def pagina_esqueci(request):
    """Renderiza a página de "Esqueci a Senha"."""
    return render(request, 'esqueci.html') 

def pagina_gamemode(request):
    """Renderiza a página de seleção de modo de jogo."""
    return render(request, 'gamemode.html') 


def pagina_perguntas_facil(request):
    """Renderiza a página de perguntas no modo fácil."""
    return render(request, 'perguntas/facil.html') 
    
def pagina_perguntas_media(request):
    """Renderiza a página de perguntas no modo médio."""
    return render(request, 'perguntas/media.html') 
    
def pagina_perguntas_dificil(request):
    """Renderiza a página de perguntas no modo difícil."""
    return render(request, 'perguntas/dificil.html') 

# Views de API (DRF) viwes de cadastro e login sempre devem vir primeiro (prioridade para  html apenas)

class CadastroUsuarioView(generics.CreateAPIView):
    """Endpoint de API para registro de novos usuários."""
    queryset = User.objects.all() 
    serializer_class = CadastroUsuarioSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
@permission_classes([AllowAny])
def fazer_login(request):
    """Endpoint de API para login (requer lógica de autenticação DRF/JWT)."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        return Response({'detail': 'Login bem-sucedido. Prossiga para obter o token JWT.'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)


# VIEWS DO MENU PRINCIPAL E FUNCIONALIDADES

@login_required(login_url='auth_login_page')
def pagina_principal(request):
    """Renderiza o template principal (home) e verifica status/foto do Perfil."""
    
    perfil = request.user.perfil if hasattr(request.user, 'perfil') else None
    is_premium = perfil.is_assinante if perfil else False
    

    context = {
        'is_premium': is_premium,
        'perfil': perfil 
    }
    return render(request, 'principal.html', context)

@login_required(login_url='auth_login_page')
def pagina_perfil(request):
    """
    Renderiza a página de perfil do usuário, passando status e formulário.
    🛑 CORRIGIDO: Removida a duplicação e garantido o RENDER 🛑
    """
    perfil = request.user.perfil if hasattr(request.user, 'perfil') else None
    is_premium = perfil.is_assinante if perfil else False
    
    
    form_foto = PerfilFotoForm(instance=perfil) 

    context = {
        'is_premium': is_premium,
       
        'perfil': perfil,
        'form_foto': form_foto, 
    }
    return render(request, 'perfil.html', context)

def pagina_ajuda(request):
    """Renderiza a página de ajuda (ajuda.html)."""
    return render(request, 'ajuda.html')


@login_required
def assinatura_page_view(request):
    """Simula o processamento da assinatura e marca o usuário como Premium."""
    
    try:
        
        if hasattr(request.user, 'perfil'):
            request.user.perfil.is_assinante = True 
            request.user.perfil.save()
            
            messages.success(request, "Parabéns! Você se tornou um usuário Premium e ganhou acesso ao BitBot!")
        else:
             messages.error(request, "Erro: Perfil do usuário não encontrado para a assinatura.")
             
    except Exception as e:
        messages.error(request, f"Erro ao processar a assinatura: {e}")
        

    return redirect('principal') 
    

@login_required
def chatbot_page(request):
    """Página de destino do BitBot Premium."""
    is_premium = request.user.perfil.is_assinante if hasattr(request.user, 'perfil') else False
    
    if not is_premium:
        messages.warning(request, "Acesso negado. Por favor, assine o BitBot Premium.")
        return redirect('principal')
        
    return render(request, 'chatbot.html') # templade ja criado


@login_required
def upload_foto_perfil(request):
    """Processa o upload da foto de perfil."""
    if request.method == 'POST':
        perfil = request.user.perfil
        
        # request.POST para dados de texto e request.FILES para o arquivo de imagem
        form = PerfilFotoForm(request.POST, request.FILES, instance=perfil)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto de perfil atualizada com sucesso!')
        else:
            messages.error(request, 'Erro ao fazer upload da foto. Verifique o formato.')
            
   
    return redirect('perfil_page')