from django.urls import path, include
from .views.index import HomeView
from .views.user import MyPage

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('mypage', MyPage.as_view(), name='mypage'),
    path('accounts/', include('allauth.urls'))
)