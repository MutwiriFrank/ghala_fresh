from django.urls import path
from .views import RegisterFarmerView, RegisterVendorView, login_page,  logout_page

app_name = 'users'

urlpatterns = [
    # token authentication
    # path('token/', loginView.as_view(), name='token_obtain_pair'), # login endpoint
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/farmer/register/', RegisterFarmerView.as_view()),
    path('api/vendor/register/', RegisterVendorView.as_view()),

  
    path('login', login_page, name="login"),
    path('logout', logout_page, name="logout")

]