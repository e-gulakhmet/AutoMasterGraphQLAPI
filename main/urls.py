from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from graphene_django.views import GraphQLView


# class HealthCheckView(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny,)
#
#     @swagger_auto_schema(responses={200: ''})
#     def get(self, request):
#         return Response(data='OK', status=status.HTTP_200_OK)


urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Health check
    # path('health', HealthCheckView.as_view()),

    # Web API automatic documentation
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Web API
    # path('token/', include('tokens.urls', namespace='tokens')),
    # path('user/', include('users.urls', namespace='users')),
    # path('master/', include('masters.urls', namespace='masters')),
    # path('register/', include('registers.urls', namespace='registers')),
    path("graphql", GraphQLView.as_view(graphiql=True)),
] + static(settings.MEDIA_PATH, document_root=settings.MEDIA_ROOT)
