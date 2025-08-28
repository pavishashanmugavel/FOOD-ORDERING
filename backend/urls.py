from django.contrib import admin
from django.urls import path
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('order/', views.order_view, name='order'),
    path('orders/', views.order_view),  # optional alias
    path('contact/', views.contact_view, name='contact'),
    path('ordersummary/', views.order_summary_view, name='order_summary'),  # ✅ Add this line
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('feedback/submit/', views.submit_feedback, name='submit_feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
]
