
from django.urls import path
from . import views
from .views import ListDocsPageView, DrafPageView, CreatePostView, CreateUpdateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.curuser, name='curuser'),
    path('all/', ListDocsPageView.as_view(), name='all'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    # path('postFile/', views.create_to_feed, name='add_file'),
    # path('addFile/', views.add_post_and_file, name='add'),

    # path('post/', views.add_docs, name='add_doc'),
    path('draf/', DrafPageView.as_view(), name='draf'),
    path('login/', views.user_login, name='login'),

    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/update', CreateUpdateView.as_view(), name='update'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='updocks/adddoc/logout.html',
                                                  next_page=None), name='logout'),
]

