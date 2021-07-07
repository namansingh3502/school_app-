from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework import status
from .models import UserProfile


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):

    profile = request.user.userprofile
    serializer = UserProfileSerializer(profile)

    return Response(serializer.data)

