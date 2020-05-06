from django.urls import path, include
from .views.index import HomeView
from .views.user import MyPage
from .views.problem import ProblemsView, SubmitView, ProblemSetView, ProblemsInSetView
from .views.manager.problem import ManageProblemsView, CreateProblemsView
from .views.manager.manager import ManageManagerView
from .views.search import user_search


urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('mypage/', MyPage.as_view(), name='mypage'),
    ####################################################
    path('manage/problem', ManageProblemsView.as_view(), name='manage_problem'),
    path('manage/problem/new', CreateProblemsView.as_view(), name='create_problem'),
    path('manage/manager', ManageManagerView.as_view(), name='manage_manager'),
    ####################################################
    path('problem', ProblemsView.as_view(), name='problems'),
    path('problem/<int:id>', SubmitView.as_view(), name='submit_problem'),
    path('problemset', ProblemSetView.as_view(), name='problemset_list'),
    path('problemset/<int:id>', ProblemsInSetView.as_view(), name='problemset_problems'),
    ####################################################
    path('search/user', user_search, name='search_user'),
    ####################################################
    path('accounts/', include('allauth.urls'))
)