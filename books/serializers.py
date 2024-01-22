from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # faqat harflardan tashkil topganligini tekshiradi
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Iltimos faqat text kiriting"
                }
            )

        return data

    def validate_title(self, title):
        if Book.objects.filter(title=title).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Bu title dbda bor"
                }
            )

    def validate_price(self, price):
        if price < 0 or price > 99999 or price == 0:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notogri kiritilgan"
                }
            )
        return price

    def validate_author(self, author):
        if Book.objects.filter(author=author).exists():
            raise ValidationError({
                "status": False,
                "message": "Bu author dbda bor"
            })
        return author

