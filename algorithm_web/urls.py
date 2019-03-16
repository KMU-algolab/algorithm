from django.urls import path, include
from .views.index import HomeView

urlpatterns = (
    path('', HomeView.as_view(template_name="index.html"), name='home'),
    path('accounts/', include('allauth.urls'))
)