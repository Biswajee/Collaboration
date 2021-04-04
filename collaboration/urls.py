"""collaboration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

'''
The project contains 5 web applications each for a given task.
However, the base URL http://127.0.0.0:8000 is included in dashboard.urls
The base URL contains links to all available applications in the project.
'''


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('dashboard.urls')),
    url(r'doc/', include('docviewer.urls')),
    url(r'slide/', include('slideviewer.urls')),
    url(r'api/', include('mediaAPI.urls')),
    url(r'd3/', include('visualizations.urls')),
]
