from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def is_phone_number(value):
    if value[0] == '+':
        for i in range(1,len(value)):
            if value[i] in '1234567890':
                pass
            else:
                raise ValidationError(
            _('%(value)s is not phone number number'),
            params={'value': value},
            )
    else:
        raise ValidationError(
            _('%(value)s has no plus at begin'),
            params={'value': value},
            )
