from django.urls import path
from . import views


app_name = 'case'
urlpatterns = [
    path('', views.pj_list, name='pj_list'),
    path('project/<int:pk>', views.pj_detail, name='pj_detail'),  # SPAにしたため不要か
]