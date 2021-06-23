from . import views
from django.urls import path
urlpatterns = [
    path("",views.user_page ,name = "user_page"),
    path('about',views.about , name = "about" ),
    path('index',views.index, name = 'index'),
    path('logout',views.logouts, name = 'logout'),
    path('accounts/login/login',views.login , name = "login"),
    path('user_page',views.test),
    path('page_of_winter',views.page_of_winter),
    path('page_of_summer',views.page_of_summer),
    path('page_of_autmn',views.page_of_autumn),
    path('page_of_spring',views.page_of_spring),
    path('email',views.user_page,name = 'user_page'),
    path('comments',views.comments,name = 'comments'),
]