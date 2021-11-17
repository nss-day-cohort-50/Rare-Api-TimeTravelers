from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rarerestapi.views import register_user, login_user
from rest_framework import routers
from rarerestapi.views import RareUserView, ReactionView, CategoryView, TagView, PostView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rareusers', RareUserView, 'rareuser')
router.register(r'reactions', ReactionView, 'reaction')
router.register(r'categories', CategoryView, 'category')
router.register(r'posts', PostView, 'post')
router.register(r'tags', TagView, 'tag')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

