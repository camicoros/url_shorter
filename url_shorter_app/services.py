from django.core.exceptions import ObjectDoesNotExist

from .utils import generate_slug


def generate_short_url(model, field: str):
    original = False
    new_short_url = ""

    while not original:
        new_short_url = generate_slug(model._meta.get_field(field).max_length)
        try:
            model.objects.get(**{field: new_short_url})
        except ObjectDoesNotExist:
            original = True

    return new_short_url
