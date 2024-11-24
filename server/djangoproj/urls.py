from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', views.home_view, name='home'),  # Updated home view
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),  # Added contact page path
    path('login/', TemplateView.as_view(template_name="index.html")),  # Added login page path
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
