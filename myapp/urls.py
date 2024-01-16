# myapp/urls.py
from django.urls import path
from .views import home, CustomLoginView, CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)