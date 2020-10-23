from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields =["username", "gender", "text"]
        
      
  
    # this function will be used for the validation 
    def clean(self): 
  
        # data from the form is fetched using super function 
        super(ContactForm, self).clean() 
          
        # extract the username and text field from the data 
        username = self.cleaned_data.get('username') 
        text = self.cleaned_data.get('text') 
  
        # conditions to be met for the username length 
        if len(username) < 5: 
            self._errors['username'] = self.error_class([ 
                'Minimum 5 characters required']) 
        if len(text) <10: 
            self._errors['text'] = self.error_class([ 
                'Post Should Contain a minimum of 10 characters']) 
  
        # return any errors if found 
        return self.cleaned_data 