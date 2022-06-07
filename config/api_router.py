from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from coachify.users.api.views import (
    ClassAPIViewSet,
    ParentAPIViewSet,
    StudentAPIViewSet,
    TeacherAPIViewSet,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

#: router.register("users", UserViewSet)
router.register("teachers", TeacherAPIViewSet)
router.register("students", StudentAPIViewSet)
router.register("classes", ClassAPIViewSet)
router.register("parents", ParentAPIViewSet)

app_name = "api"
urlpatterns = router.urls
