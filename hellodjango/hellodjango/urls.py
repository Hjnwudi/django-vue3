"""
URL configuration for hellodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fanju/', include('fanju.urls')),
    path('live/', include('live.urls')),
    path('students/', views.get_students),
    path('students/query/', views.query_students),
    path('sno/check/', views.is_exists_sno),
    path('students/add/', views.add_students),
    path('students/update/', views.update_students),
    path('students/delete/', views.delete_students),
    path('students/deleteall/', views.delete_all_students),
    path('excel/upload/', views.import_students_excel),
    path('students/imageload/', views.upload),
    path('excel/export/', views.export_student_excel)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)