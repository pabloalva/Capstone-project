from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

#from django.conf import settings
#from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/items', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    #path('about/', views.about, name="about"),
    #path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    #path('menu/', views.menu, name="menu"),
    #path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]