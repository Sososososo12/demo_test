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
from django.views.generic.base import RedirectView
from django.views import static
from django.conf import settings

from sports.views import getsearchhtml, gettable,searchindex,getsta_index,getsta_table1,getsta_core_fund_table,getsta_core_fund_pic,getsta_pa_org_table,getsta_pa_org_pic,getsta_pa_dis_table,getsta_pa_dis_pic,getsta_bo_table,getsta_bo_quote_pic

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
    url('core_quote/',getsta_table1,name="static_table1"),
    url('core_fund/',getsta_core_fund_table,name="static_table2"),
    url('core_fund_pic/',getsta_core_fund_pic,name="static_pic2"),
    url('pa_org/',getsta_pa_org_table,name="static_table3"),
    url('pa_org_pic/',getsta_pa_org_pic,name="static_pic3"),
    url('pa_dis/',getsta_pa_dis_table,name="static_table4"),
    url('pa_dis_pic/',getsta_pa_dis_pic,name="static_pic4"),
    url('book_quote/',getsta_bo_table,name="static_table5"),
    url('book_quote_pic/',getsta_bo_quote_pic,name="static_pic5"),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/images/favicon.ico')),



    # 添加DEBUG=True时的static_root路径
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static'),
]
# 表格和图片信息分开，标题改进