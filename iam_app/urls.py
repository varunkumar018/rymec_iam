from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, SchemeViewSet, BatchViewSet, StaffFilterView, SubjectViewSet, StaffViewSet, StudentViewSet, IAMarksViewSet,StudentFilterView

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
    path('varun/ia/', StudentFilterView.as_view(), name='student_filter'),  # Add path to StudentFilterView

    path('filter/staff/', StaffFilterView.as_view(), name='staff_filter'),  # Add path to StaffFilterView

]
