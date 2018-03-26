"""demo_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
# from django.urls import path
from django.views.generic import TemplateView

from sports.views import getsearchhtml, gettable,searchindex,getsta_index,getsta_table1,getsta_co_fund_table,getsta_pa_org_table,getsta_pa_dis_table,getsta_bo_table

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url('form/', getform),
    # url('table/', gettable),
    # url('search/',gettable),
    url('search/',searchindex),
    url('^$', TemplateView.as_view(template_name='index_welcome.html'), name="index"),
    # url('search_url/',TemplateView.as_view(template_name='search_url.html'),name="searchhtml"),
    # url('form/',searchindex)
    url('search_url/',searchindex,name="searchhtml"),
    url('sta_index/',getsta_index,name="static_index"),
    url('excel_djangonew2/',getsta_table1,name="static_table1"),
    url('core_fund/',getsta_co_fund_table,name="static_table2"),
    url('paper_organ/',getsta_pa_org_table,name="static_table3"),
    url('paper_district/',getsta_pa_dis_table,name="static_table4"),
    url('book_sta/',getsta_bo_table,name="static_table5"),
]
