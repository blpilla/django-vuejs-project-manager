
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ClienteViewSet, ProjetoViewSet, AtividadeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'atividades', AtividadeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),  # Certifique-se de incluir o roteador aqui
]
