from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Order, Product

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'discord_username', 'whatsapp', 'payment_proof']
        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'discord_username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم حساب Discord'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم WhatsApp'}),
            'payment_proof': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور الجديدة'}),
        label='كلمة المرور الجديدة',
        min_length=6
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'}),
        label='تأكيد كلمة المرور'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('new_password')
        confirm = cleaned_data.get('confirm_password')
        
        if password and confirm and password != confirm:
            raise forms.ValidationError('كلمات المرور غير متطابقة')
        return cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'product_type', 'platform', 'image', 'image_url', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المنتج'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'وصف المنتج الكامل'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'السعر بالجنيه'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_type': forms.Select(attrs={'class': 'form-control'}),
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'أو ضع رابط الصورة (https://...)'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # إضافة checkboxes للتاجات
        if self.instance and self.instance.pk and self.instance.tags:
            selected_tags = self.instance.get_tags_list()
        else:
            selected_tags = []
        
        for tag_value, tag_label in Product.TAG_CHOICES:
            field_name = f'tag_{tag_value}'
            self.fields[field_name] = forms.BooleanField(
                required=False,
                initial=tag_value in selected_tags,
                label=tag_label
            )
        
        # إضافة FEATURE_CHOICES
        self.fields['features'] = forms.MultipleChoiceField(
            choices=Product.FEATURE_CHOICES,
            required=False,
            widget=forms.CheckboxSelectMultiple
        )
    
    def clean(self):
        cleaned_data = super().clean()
        # جمع التاجات المختارة
        selected_tags = []
        for tag_value, tag_label in Product.TAG_CHOICES:
            field_name = f'tag_{tag_value}'
            if cleaned_data.get(field_name):
                selected_tags.append(tag_value)
        
        if len(selected_tags) < 2 or len(selected_tags) > 5:
            raise forms.ValidationError('يجب اختيار من 2 إلى 5 تاجات')
        
        cleaned_data['selected_tags'] = selected_tags
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        selected_tags = self.cleaned_data.get('selected_tags', [])
        instance.tags = ', '.join(selected_tags)
        if commit:
            instance.save()
        return instance
