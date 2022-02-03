from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('detail/<int:id>', views.detail_view, name='detail'),
    path('main/<int:id>',views.qmain,name="qmain"),
]