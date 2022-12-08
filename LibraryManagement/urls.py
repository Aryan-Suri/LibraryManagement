from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('addStudent/', views.addStudent, name='AddStudent'),
    path('addBook/', views.addBook, name='AddBook'),
    path('showBooks/', views.showBooks, name='showBooks'),
    path('update/<int:book_id>', views.update_task, name='updateTasks'),
    path('delete/<int:book_id>', views.delete_task, name="delete"),
    path('search_task', views.search, name="search"),
    path('issue_book', views.issue, name="issue"),
]