from django import forms

class TutorialDropDownForm(forms.Form):
    OPTIONS = [
        ('option1', 'the first option'),
        ('option2', 'the second option'),
        ('option3', 'the third option'),
    ]
    choice_field = forms.ChoiceField(choices=OPTIONS, label="Please select an option")