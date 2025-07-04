from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    login_view, 
    register_view, 
    home_view, 
    create_event, 
    view_event, 
    logout_view, 
    delete_event, 
    edit_event_view, 
    gallery_views,
    get_started_view,
    users_events,
    event_list_view
    )

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('gallery/', gallery_views, name='gallery'),
    path('add_Event/', create_event, name='add_event'),
    path('getStarted/', get_started_view, name="get_started"),
    path('view_event/<int:pk>/details/', view_event, name='view_event'),
    path('logout/', logout_view, name='logout'),
    path('delete_event/<int:pk>/', delete_event, name='delete_event'),
    path('edit_event/<int:pk>', edit_event_view, name='edit_event'),
    path('myEvents/', users_events, name="my_events"),
    path('events-list', event_list_view, name="event_list")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)