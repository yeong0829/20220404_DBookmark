from django import forms

from bookmark.models import Bookmark


class BookmarkCreationForm(forms.ModelForm):
    url = forms.CharField(label='링크', widget=forms.TextInput)

    class Meta:
        model = Bookmark
        fields = ['name', 'url']

    def save(self, commit=True):
       new_bookmark = Bookmark.objects.create(
           name=self.cleaned_data('name'),  # 사용자가 입력한 내용을 clean_name()하고 깨끗해진 것 가져오기
           url=self.cleaned_data('url'),   # 사용자가 입력한 내용을 clean_url()하고 깨끗해진 것 가져오기
       )
       return new_bookmark