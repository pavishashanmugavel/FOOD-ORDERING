from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('order/', views.order_view, name='order'),
    path('contact/', views.contact_view, name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order-summary/', views.order_summary_view, name='order_summary'),
     path('submit/', views.submit_feedback, name='submit_feedback'),
    path('success/', views.feedback_success, name='feedback_success'),
]
