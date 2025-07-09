from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # <-- ESSA É A LINHA CRUCIAL

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contas/login/', auth_views.LoginView.as_view(), name='login'),

    path('contas/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('', include('acervo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)