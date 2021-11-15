from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
        path( '', views.HomeView.as_view(), name='home' ), 
    path( 'section1_1/', views.Section1_1View.as_view(), name='section1_1' ), 
    path( 'section1_2/', views.Section1_2View.as_view(), name='section1_2' ), 
    path( 'section1_3/', views.Section1_3View.as_view(), name='section1_3' ), 
    path( 'help1_1/', views.Help1_1View.as_view(), name='help1_1' ), 
    path( 'help1_2/', views.Help1_2View.as_view(), name='help1_2' ), 
    path( 'help1_3/', views.Help1_3View.as_view(), name='help1_3' ), 
]