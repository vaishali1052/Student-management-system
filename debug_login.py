import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_management_system.settings")
django.setup()

from student_management_app.models import CustomUser
from django.contrib.auth import authenticate

print("=== All Users ===")
for u in CustomUser.objects.all():
    print(f"  email:{u.email} | username:{u.username} | type:{u.user_type} | active:{u.is_active}")

print("\n=== Resetting all passwords to admin123 ===")
for u in CustomUser.objects.all():
    u.set_password("admin123")
    u.save()

print("\n=== Testing authenticate ===")
for u in CustomUser.objects.all():
    result = authenticate(username=u.email, password="admin123")
    print(f"  {u.email} -> {'OK type:'+str(u.user_type) if result else 'FAIL'}")
