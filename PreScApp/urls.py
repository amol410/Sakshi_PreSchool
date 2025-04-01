from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),    
    path('facility/', views.facility, name='facility'),
    path('projects/', views.projects, name='projects'), 
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'), 
    path('classes/', views.classes, name='classes'),
    path('call-to-action/', views.call_to_action, name='call-to-action'),
    path('appointment/', views.appointment, name='appointment'),
    path('404/', views.page_not_found, name='page-not-found'),

]       