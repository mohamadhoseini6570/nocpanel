"""nocpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
# from django.conf import settings
from django.conf.urls.static import static
# from django.views.i18n import JavaScriptCatalog

admin.site.site_header = 'Network Operation Center Panel'
urlpatterns = [
    # path('admin/doc/', include('django.contrib.admindocs.urls')),
    # path('',  name='index'),
    path('admin/', admin.site.urls),
    path('', include('contract.urls')),
    path('', include('customer.urls')),
    path('', include('agent.urls')),
    path('', include('cloud.urls')),
    path('', include('dashboard.urls')),
    path('', include('ip.urls')),
    # path('js-catalog', JavaScriptCatalog.as_view(), name='js-catalog')
]
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += [
    # re_path(r'^accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
