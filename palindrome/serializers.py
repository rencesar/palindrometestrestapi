from rest_framework import serializers


class StringPalindrome(serializers.Serializer):
    string = serializers.CharField(required=True, max_length=200)

    def validate_string(self, value):
        reverse = value[::-1]
        if reverse != value:
            raise serializers.ValidationError('Given string is not palindrome')
        return value
