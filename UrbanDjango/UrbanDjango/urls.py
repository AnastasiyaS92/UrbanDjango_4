from django.contrib import admin
from django.urls import path
from task2.views import class_template,func_template
from task4.views import platform_page, games_page, cart_page
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = {
    path('admin/', admin.site.urls),
    path('class/', class_template.as_view()),
    path('func/', func_template),
    path('platform/', platform_page),
    path('games/', games_page),
    path('cart/', cart_page),
    path('', sign_up_by_django),
    path('sign/', sign_up_by_html)
}
