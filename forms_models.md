# Formularios a partir de modelos

		from django.forms import ModelForm
		from myapp.models import Article		

		# Create the form class.
		class ArticleForm(ModelForm):
		     class Meta:
		         model = Article
		         fields = ['pub_date', 'headline', 'content', 'reporter']		

		# Creating a form to add an article.
		form = ArticleForm()

## Relación entre el campo del módelo y el campo del formulario:

Model field 			Form field
AutoField 				Not represented in the form
BigIntegerField 		IntegerField with min_value set to -9223372036854775808 and max_value set to 9223372036854775807.
BooleanField 			BooleanField
CharField 				CharField with max_length set to the model field’s max_length
CommaSeparatedIntegerField 	CharField
DateField 	DateField
DateTimeField 	DateTimeField
DecimalField 	DecimalField
EmailField 	EmailField
FileField 	FileField
FilePathField 	FilePathField
FloatField 	FloatField
ForeignKey 	ModelChoiceField (see below)
ImageField 	ImageField
IntegerField 	IntegerField
IPAddressField 	IPAddressField
GenericIPAddressField 	GenericIPAddressField
ManyToManyField 	ModelMultipleChoiceField (see below)
NullBooleanField 	CharField
PositiveIntegerField 	IntegerField
PositiveSmallIntegerField 	IntegerField
SlugField 	SlugField
SmallIntegerField 	IntegerField
TextField 	CharField with widget=forms.Textarea
TimeField 	TimeField
URLField 	URLField