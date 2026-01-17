from django.urls import path
from . import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static
import os

urlpatterns = [
    path('', views.home, name='home'),
    path('Aboutus/', views.about, name='Aboutus'),
    path('contact/', views.contact, name='contact'),
    path('Courses/', views.courses, name='Courses'),
    path('Defence/', views.defence, name='Defence'),
    path('Engineering/', views.engineering, name='Engineering'),
    path('Law/', views.law, name='Law'),
    path('Medical/', views.medical, name='Medical'),
    path('Register/', views.register, name='Register'),
    path('contactus/', views.contact, name='contactus'),
    path('government/', views.government, name='government'),
    path('others/', views.others, name='others'),
]

# Serve static files (like images) during development
if settings.DEBUG:
    template_images_dir = os.path.join(settings.BASE_DIR, 'careerBackend', 'templates', 'careerBackend', 'images')
    urlpatterns += static('/images/', document_root=template_images_dir)
    urlpatterns += static('/contactus/images/', document_root=template_images_dir)
    urlpatterns += static('/Register/images/', document_root=template_images_dir)

    css_dir = os.path.join(settings.BASE_DIR, 'careerBackend', 'templates', 'careerBackend', 'CSS')
    urlpatterns += static('/CSS/', document_root=css_dir)
    urlpatterns += static('/Register/CSS/', document_root=css_dir)
    urlpatterns += static('/contactus/CSS/', document_root=css_dir)
