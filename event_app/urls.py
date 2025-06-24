from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, register_view, home_view, create_event

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('add_Event/', create_event, name='add_event'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)