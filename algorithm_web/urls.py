from django.urls import path, include
from .views.index import HomeView
from .views.user import MyPage
from .views.problem import Problems, Submit
from .views.manager.problem import ManageProblems, CreateProblems


urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('mypage/', MyPage.as_view(), name='mypage'),
    ####################################################
    path('manage/problem', ManageProblems.as_view(), name='manage_problem'),
    path('manage/problem/new', CreateProblems.as_view(), name='create_problem'),
    # path('manage/manager', ManageManager.as_view(), name='manage_manager'),
    # path('manage/manager/new', CreateManager.as_view(), name='create_manager'),
    ####################################################
    path('problem', Problems.as_view(), name='problem_list'),
    path('problem/submit/<int:id>', Submit.as_view(), name='submit_problem'),
    ####################################################
    path('accounts/', include('allauth.urls'))
)