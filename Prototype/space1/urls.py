from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /machine
    path('iolist', views.iolist, name='iolist'),  # /machine/iolist

    path('<int:n>', views.detail, name='detail'), # 일자별 List
    path('<int:n>/short', views.short, name='short'), # Machine의 간단한 정보
    path('<int:n>/<int:m>', views.view, name='view'), # 문서의 데이터
    
    path('<int:n>/edit', views.edit, name='edit'),
    path('<int:n>/<int:m>/edit', views.edit2, name='edit2'),
    path('<int:n>/edit/delete', views.edit_delete, name='edit_delete'),
]
