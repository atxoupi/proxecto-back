from django.urls import path

from .views import Register, Login, Logout, Me, ChangePassword

urlpatterns = [
    # Nun primeiro momento non me interesa o rexistro de usuarios, pero para futuras versións pode ser útil
    # path("register", Register.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
    path("me", Me.as_view(), name="me"),
    path("change-password", ChangePassword.as_view(), name="change-password"),
]