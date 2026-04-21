from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        # Always allow these for everyone
        always_allow = [
            "django.contrib.auth.views",
            "django.contrib.admin.sites",
            "django.contrib.admin.options",
            "django.contrib.admin.actions",
            "django.views.static",
            "student_management_app.views",
        ]

        if modulename.startswith("health_check"):
            return None
        if modulename.startswith("django.contrib.admin"):
            return None
        if modulename in always_allow:
            return None

        if user.is_authenticated:
            if user.user_type == "1":
                # HOD — allow HodViews only
                if modulename == "student_management_app.HodViews":
                    return None
                # Already on admin_home, don't redirect loop
                return HttpResponseRedirect(reverse("admin_home"))

            elif user.user_type == "2":
                # Staff
                if modulename in [
                    "student_management_app.StaffViews",
                    "student_management_app.EditResultVIewClass",
                ]:
                    return None
                return HttpResponseRedirect(reverse("staff_home"))

            elif user.user_type == "3":
                # Student
                if modulename == "student_management_app.StudentViews":
                    return None
                return HttpResponseRedirect(reverse("student_home"))

            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            # Not logged in
            allowed_paths = [
                reverse("show_login"),
                reverse("do_login"),
            ]
            if request.path in allowed_paths:
                return None
            return HttpResponseRedirect(reverse("show_login"))
