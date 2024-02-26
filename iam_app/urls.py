from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, SchemeViewSet, BatchViewSet, SubjectViewSet, StaffViewSet, StudentViewSet, IAMarksViewSet

router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'schemes', SchemeViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'students', StudentViewSet)
router.register(r'iamarks', IAMarksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
