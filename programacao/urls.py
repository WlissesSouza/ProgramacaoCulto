from django.urls import path, include
from . import views

urlpatterns = [
    path('prog/v1', views.get_programacao, name='get_programacao_v1'),
    path('prog/<int:programacao>', views.get_by_programacao, name='programacao_dia'),
    path('data/', views.programacao_manage, name='data'),

]
