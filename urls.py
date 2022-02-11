from django.urls import path
from . import views

urlpatterns = [
       path('windex2',views.windex2,name='windex2'),
       path('wproduct/<str:category>/',views.wproduct,name='wproduct'),
       path('wabout',views.wabout,name='wabout'),
       path('wcontact',views.wcontact,name='wcontact'),
       path('view_contact',views.view_contact,name='view_contact'),
       path('wcart',views.wcart,name='wcart'),
       path('wcheckout',views.wcheckout,name='wcheckout'),
       path('w_check',views.w_check,name='w_check'),
       path('cart_update',views.cart_update,name='cart_update'),
       path('wsinglepro/<int:fid>/',views.wsinglepro,name='wsinglepro'),
       path('wrecipe',views.wrecipe,name='wrecipe'),
       path('wsinglerecipe/<int:frid>/',views.wsinglerecipe,name='wsinglerecipe'),
       path('wlogin',views.wlogin,name='wlogin'),
       path('wlogout',views.wlogout,name='wlogout'),
       path('wreg',views.wreg,name='wreg'),
       path('wdisplay',views.wdisplay,name='wdisplay'),
       path('wlog',views.wlog,name='wlog'),
       path('wdelete/<int:did>/',views.wdelete,name='wdelete'),
       path('fish_cart/<int:sid>/',views.fish_cart,name='fish_cart'),
       path('viewcheck',views.viewcheck,name='viewcheck'),
       path('Fdelete/<int:cid>/',views.Fdelete,name='Fdelete')
]