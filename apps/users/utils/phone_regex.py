from django.core.validators import RegexValidator

UZB_PHONE_VALIDATOR = RegexValidator(regex=r"^(\+998)(\d{9})$", message="Неправильный формат номера. Пример +998(XX)XXX-XX-XX")