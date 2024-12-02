from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sub=<int:sub_id>&per=<int:per_page>', views.dashboard, name='Dashboard'),
    path('report/sub<int:sub_id>', views.AltogetherView.as_view(), name='altogether_view'),
    path('get_total_runtime', views.AltogetherView.get_total_runtime, name='get_total_runtime'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)