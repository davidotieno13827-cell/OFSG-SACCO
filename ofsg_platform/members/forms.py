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
    profile_picture = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'w-full text-sm text-slate-600'}))
    passport_photo = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'w-full text-sm text-slate-600'}))
    id_document = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'w-full text-sm text-slate-600'}))

    def _validate_uploaded_file(self, uploaded_file, allowed_content_types, field_label):
        if not uploaded_file:
            return uploaded_file

        max_size = 5 * 1024 * 1024
        if uploaded_file.size > max_size:
            raise forms.ValidationError(f"{field_label} must be smaller than 5MB.")

        if uploaded_file.content_type not in allowed_content_types:
            raise forms.ValidationError(
                f"{field_label} must be one of: {', '.join(allowed_content_types)}."
            )
        return uploaded_file

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

    def clean_profile_picture(self):
        return self._validate_uploaded_file(
            self.cleaned_data.get('profile_picture'),
            ['image/jpeg', 'image/png'],
            'Profile picture'
        )

    def clean_passport_photo(self):
        return self._validate_uploaded_file(
            self.cleaned_data.get('passport_photo'),
            ['image/jpeg', 'image/png'],
            'Passport photo'
        )

    def clean_id_document(self):
        return self._validate_uploaded_file(
            self.cleaned_data.get('id_document'),
            ['application/pdf', 'image/jpeg', 'image/png'],
            'ID document'
        )

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
        for field_name in ('profile_picture', 'passport_photo', 'id_document'):
            uploaded_file = self.cleaned_data.get(field_name)
            if uploaded_file:
                setattr(user, field_name, uploaded_file)
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    def _validate_uploaded_file(self, uploaded_file, allowed_content_types, field_label):
        if not uploaded_file:
            return uploaded_file

        max_size = 5 * 1024 * 1024
        if uploaded_file.size > max_size:
            raise forms.ValidationError(f"{field_label} must be smaller than 5MB.")

        if uploaded_file.content_type not in allowed_content_types:
            raise forms.ValidationError(
                f"{field_label} must be one of: {', '.join(allowed_content_types)}."
            )
        return uploaded_file

    def clean_profile_picture(self):
        return self._validate_uploaded_file(
            self.cleaned_data.get('profile_picture'),
            ['image/jpeg', 'image/png'],
            'Profile picture'
        )

    def clean_passport_photo(self):
        return self._validate_uploaded_file(
            self.cleaned_data.get('passport_photo'),
            ['image/jpeg', 'image/png'],
            'Passport photo'
        )

    def clean_id_document(self):
        return self._validate_uploaded_file(
            self.cleaned_data.get('id_document'),
            ['application/pdf', 'image/jpeg', 'image/png'],
            'ID document'
        )
    class Meta:
        model = Member
        fields = [
            'next_of_kin_name',
            'next_of_kin_phone',
            'guardian_1',
            'guardian_2',
            'profile_picture',
            'passport_photo',
            'id_document',
        ]
        widgets = {
            'next_of_kin_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'next_of_kin_phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'guardian_1': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'guardian_2': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'profile_picture': forms.FileInput(attrs={'class': 'w-full text-sm text-slate-600'}),
            'passport_photo': forms.FileInput(attrs={'class': 'w-full text-sm text-slate-600'}),
            'id_document': forms.FileInput(attrs={'class': 'w-full text-sm text-slate-600'}),
        }
