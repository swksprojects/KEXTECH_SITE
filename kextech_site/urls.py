from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import cart.urls
import shop.urls
import orders.urls
import payment.urls
import paypal.standard.ipn.urls
import blog.urls
import home.urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include(cart.urls, namespace='cart')),
    url(r'^orders/', include(orders.urls, namespace='orders')),
    url(r'paypal/', include(paypal.standard.ipn.urls)),
    url(r'payment', include(payment.urls, namespace='payment')),
    url(r'^blog/', include(blog.urls, namespace='blog', app_name='blog')),
    url(r'^products/', include(shop.urls, namespace='shop')),
    url(r'^', include(home.urls, namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
