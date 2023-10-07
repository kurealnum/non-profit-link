from django import forms


def create_big_form(*forms) -> list[forms.ModelForm]:
    return [form for form in forms]
