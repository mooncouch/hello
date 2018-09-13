from django.urls import path

from . import views

urlpatterns = [
    # ex: /journal/
    path('', views.index, name='index'),
    # ex: /journal/1/
    path('<int:author_id>/', views.detail, name='author'),
    # ex: /journal/1/entry/
    path('<int:author_id>/entry/', views.entry_sum, name='entry_sum'),
    # ex: /polls/5/vote/
    path('<int:author_id>/summary/', views.summary, name='summary'),
    #how to make a view that populates based off of entry_id
    path('<int:author_id>/entry/<int:entry_id>', views.entry, name='entry'),
]

