from rest_framework.response import Response
from rest_framework.views import APIView

from palindrome.serializers import StringPalindrome


class CheckPalindrome(APIView):
    """
    View to check if given string is palindrome or not.

    * If palindrome return 200
    * Else return 400
    """
    serializer_class = StringPalindrome

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
