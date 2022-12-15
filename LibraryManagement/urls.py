from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('addBook/', views.addBook, name='AddBook'),
    path('showBooks/', views.showBooks, name='showBooks'),
    path('update/<int:book_id>', views.update_book, name='updateBooks'),
    path('delete/<int:book_id>', views.delete_book, name="delete"),
    path('search_task', views.search, name="search"),
    path('issue_book/<int:book_id>/<int:returned>', views.issue, name="issue"),
]