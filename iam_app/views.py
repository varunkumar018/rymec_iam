from rest_framework import viewsets, permissions
from .models import Branch, Scheme, Batch, Subject, Staff, Student, IA_marks
from .serializers import BranchSerializer, SchemeSerializer, BatchSerializer, SubjectSerializer, StaffSerializer, StudentSerializer, IAMarksSerializer
from django.contrib.auth import get_user_model
from users.permissions import IsClgAdmin, IsDeptAdmin, IsStaff, IsStudent



class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsClgAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsClgAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsClgAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsClgAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]


class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsClgAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsClgAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsClgAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action in "create":
    #         permission_classes = [IsDeptAdmin]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsDeptAdmin]
    #     elif self.action == "destroy":
    #         permission_classes = [IsDeptAdmin]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]


class IAMarksViewSet(viewsets.ModelViewSet):
    queryset = IA_marks.objects.all()
    serializer_class = IAMarksSerializer

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action in "create":
    #         permission_classes = [IsStaff]  
    #     elif self.action in ["update", "partial_update"]:
    #         permission_classes = [IsStaff]
    #     elif self.action == "destroy":
    #         permission_classes = [IsStaff]
    #     else:
    #         permission_classes = [permissions.AllowAny]  
    #     return [permission() for permission in permission_classes]
