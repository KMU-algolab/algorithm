from django.urls import path, include
from .views.index import HomeView
from .views.user import MyPage
from .views.manager.problem import Problems


urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('mypage/', MyPage.as_view(), name='mypage'),
    path('manage/problem', Problems.as_view(), name='manage_problem'),
    path('accounts/', include('allauth.urls'))
)