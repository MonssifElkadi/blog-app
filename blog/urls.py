from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('<int:id>/' , views.detail , name='detail'),
    path('create/',views.create , name="create"),
    path('edit/<int:id>/' , views.modify , name="edit"),
    path('delete/<int:id>/' , views.delete, name="delete")
]