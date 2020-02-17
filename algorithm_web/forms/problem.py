from django import forms
from ..models.problem import Problem, TestCase


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ('problem_name', 'problem_text', 'limit_time', 'limit_memory', 'scoring_type', 'checker_code', 'level', 'info')

        widgets = {
            'problem_name': forms.TextInput(attrs={'class': 'form-control'}),
            'problem_text': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 30}),
            'level': forms.HiddenInput(),
            'scoring_type': forms.HiddenInput(),
            'info': forms.Select(attrs={'class': 'form-control'}),
            'checker_code': forms.Textarea(attrs={'class': 'form-control'}),
            'limit_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'limit_memory': forms.NumberInput(attrs={'class': 'form-control'})
        }


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ('input', 'output')

        widgets = {
            'input': forms.TextInput(attrs={'class': 'form-control',
                                            'style': 'width: 19vw; height: 5vw; display: inline-block; margin-left: 0.5vw; margin-right: 0.5vw'}),
            'output': forms.TextInput(attrs={'class': 'form-control',
                                             'style': 'width: 19vw; height: 5vw; display: inline-block; margin-left: 0.5vw; margin-right: 0.5vw'})
        }

class InputOnlyForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ('input',)

        widgets = {
            'input': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 19vw; height: 5vw; display: inline-block; margin-left: 0.5vw'}),
        }


TestCaseFormset = forms.formset_factory(TestCaseForm, extra=1)
InputOnlyFormset = forms.formset_factory(InputOnlyForm, extra=1)
