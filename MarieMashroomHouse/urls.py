from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from Models.views import (HOME_PAGE,BLOG_PAGE,REGISTER_PAGE,INCOMMING_MESSAGE_PAGE,PRODUCT_DETAILS,
                    LOGIN_PAGE,SETTING_PAGE,BUY_PAGE,LOGOUT_PAGE,UPLOAD_BLOG_PAGE,HOME_DELEVERY_INFORMATION,
                    UPLOAD_PRODUCT,PUBLIC_PROFILE_PAGE,FINDE_FRIEND,FACE_TO_FACE_MESSAGE,
                    KURIAR_DELEVERY_INFORMATION,UPLOAD_VIDEOS,VIDEOS_CONTENT,NOTIFICATON_PAGE_VIEW,

                    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HOME_PAGE.as_view(),name='HOME_PAGE'),
    path('REGISTER_PAGE', REGISTER_PAGE.as_view(),name='REGISTER_PAGE'),
    path('LOGIN_PAGE', LOGIN_PAGE.as_view(),name='LOGIN_PAGE'),
    path('<pk>/BLOG_PAGE', BLOG_PAGE.as_view(),name='BLOG_PAGE'),
    path('<pk>/BUY_PAGE', BUY_PAGE.as_view(),name='BUY_PAGE'),
    path('LOGOUT_PAGE', LOGOUT_PAGE.as_view(),name='LOGOUT_PAGE'),
    path('<pk>/UPLOAD_PRODUCT', UPLOAD_PRODUCT.as_view(),name='UPLOAD_PRODUCT'),
    path('<pk>/SETTING_PAGE', SETTING_PAGE.as_view(),name='SETTING_PAGE'),
    path('<pk>/FINDE_FRIEND', FINDE_FRIEND.as_view(),name='FINDE_FRIEND'),
    path('<pk>/PUBLIC_PROFILE_PAGE', PUBLIC_PROFILE_PAGE.as_view(),name='PUBLIC_PROFILE_PAGE'),
    path('<pk>/FACE_TO_FACE_MESSAGE', FACE_TO_FACE_MESSAGE.as_view(),name='FACE_TO_FACE_MESSAGE'),
    path('<pk>/INCOMMING_MESSAGE_PAGE', INCOMMING_MESSAGE_PAGE.as_view(),name='INCOMMING_MESSAGE_PAGE'),
    path('<pk>/UPLOAD_BLOG_PAGE', UPLOAD_BLOG_PAGE.as_view(),name='UPLOAD_BLOG_PAGE'),
    path('<pk>/PRODUCT_DETAILS', PRODUCT_DETAILS.as_view(),name='PRODUCT_DETAILS'),
    path('<pk>/HOME_DELEVERY_INFORMATION', HOME_DELEVERY_INFORMATION.as_view(),name='HOME_DELEVERY_INFORMATION'),
    path('<pk>/KURIAR_DELEVERY_INFORMATION', KURIAR_DELEVERY_INFORMATION.as_view(),name='KURIAR_DELEVERY_INFORMATION'),
    path('<pk>/UPLOAD_VIDEOS', UPLOAD_VIDEOS.as_view(),name='UPLOAD_VIDEOS'),
    path('<pk>/VIDEOS_CONTENT', VIDEOS_CONTENT.as_view(),name='VIDEOS_CONTENT'),
    path('<pk>/NOTIFICATON_PAGE_VIEW', NOTIFICATON_PAGE_VIEW.as_view(),name='NOTIFICATON_PAGE_VIEW'),



] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
