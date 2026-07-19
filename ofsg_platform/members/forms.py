from django import forms
from .models import Contribution, Fine, Member


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['member', 'amount', 'contribution_type']
        widgets = {
            'member': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'contribution_type': forms.Select(choices=[
                ('Monthly', 'Monthly Contribution'),
                ('AGM', 'AGM Fee'),
                ('Welfare', 'Welfare/Social'),
            ], attrs={'class': 'w-full p-2 border rounded'}),
        }


class FineForm(forms.ModelForm):
    class Meta:
        model = Fine
        fields = ['member', 'fine_type', 'amount', 'is_paid']
        widgets = {
            'member': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'fine_type': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'h-4 w-4 rounded border-gray-300'}),
        }


class MemberRegistrationForm(forms.Form):
    input_attrs = {
        'class': 'w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-[color:var(--ofsg-green)]'
    }
    username = forms.CharField(required=True, widget=forms.TextInput(attrs=input_attrs))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs=input_attrs))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs=input_attrs))
    next_of_kin_name = forms.CharField(required=False, widget=forms.TextInput(attrs=input_attrs))
    next_of_kin_phone = forms.CharField(required=False, widget=forms.TextInput(attrs=input_attrs))
    guardian_1 = forms.CharField(required=False, widget=forms.TextInput(attrs=input_attrs))
    guardian_2 = forms.CharField(required=False, widget=forms.TextInput(attrs=input_attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=input_attrs), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=input_attrs), required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')
        if email and Member.objects.filter(email__iexact=email).exists():
            self.add_error('email', 'A user with that email already exists.')
        return cleaned_data

    def save(self, commit=True):
        user = Member.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            phone_number=self.cleaned_data['phone_number'],
            next_of_kin_name=self.cleaned_data.get('next_of_kin_name', ''),
            next_of_kin_phone=self.cleaned_data.get('next_of_kin_phone', ''),
            guardian_1=self.cleaned_data.get('guardian_1', ''),
            guardian_2=self.cleaned_data.get('guardian_2', ''),
        )
        user.is_active = False
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'next_of_kin_name',
            'next_of_kin_phone',
            'guardian_1',
            'guardian_2',
        ]
        widgets = {
            'next_of_kin_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'next_of_kin_phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'guardian_1': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'guardian_2': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        }
