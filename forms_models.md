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


<table class="docutils">
<colgroup>
<col width="41%" />
<col width="59%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Model field</th>
<th class="head">Form field</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.AutoField" title="django.db.models.AutoField"><tt class="xref py py-class docutils literal"><span class="pre">AutoField</span></tt></a></td>
<td>Not represented in the form</td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.BigIntegerField" title="django.db.models.BigIntegerField"><tt class="xref py py-class docutils literal"><span class="pre">BigIntegerField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.IntegerField" title="django.forms.IntegerField"><tt class="xref py py-class docutils literal"><span class="pre">IntegerField</span></tt></a> with
<tt class="docutils literal"><span class="pre">min_value</span></tt> set to -9223372036854775808
and <tt class="docutils literal"><span class="pre">max_value</span></tt> set to 9223372036854775807.</td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.BooleanField" title="django.db.models.BooleanField"><tt class="xref py py-class docutils literal"><span class="pre">BooleanField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.BooleanField" title="django.forms.BooleanField"><tt class="xref py py-class docutils literal"><span class="pre">BooleanField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.CharField" title="django.db.models.CharField"><tt class="xref py py-class docutils literal"><span class="pre">CharField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.CharField" title="django.forms.CharField"><tt class="xref py py-class docutils literal"><span class="pre">CharField</span></tt></a> with
<tt class="docutils literal"><span class="pre">max_length</span></tt> set to the model field&#8217;s
<tt class="docutils literal"><span class="pre">max_length</span></tt></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.CommaSeparatedIntegerField" title="django.db.models.CommaSeparatedIntegerField"><tt class="xref py py-class docutils literal"><span class="pre">CommaSeparatedIntegerField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.CharField" title="django.forms.CharField"><tt class="xref py py-class docutils literal"><span class="pre">CharField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.DateField" title="django.db.models.DateField"><tt class="xref py py-class docutils literal"><span class="pre">DateField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.DateField" title="django.forms.DateField"><tt class="xref py py-class docutils literal"><span class="pre">DateField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.DateTimeField" title="django.db.models.DateTimeField"><tt class="xref py py-class docutils literal"><span class="pre">DateTimeField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.DateTimeField" title="django.forms.DateTimeField"><tt class="xref py py-class docutils literal"><span class="pre">DateTimeField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.DecimalField" title="django.db.models.DecimalField"><tt class="xref py py-class docutils literal"><span class="pre">DecimalField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.DecimalField" title="django.forms.DecimalField"><tt class="xref py py-class docutils literal"><span class="pre">DecimalField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.EmailField" title="django.db.models.EmailField"><tt class="xref py py-class docutils literal"><span class="pre">EmailField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.EmailField" title="django.forms.EmailField"><tt class="xref py py-class docutils literal"><span class="pre">EmailField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.FileField" title="django.db.models.FileField"><tt class="xref py py-class docutils literal"><span class="pre">FileField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.FileField" title="django.forms.FileField"><tt class="xref py py-class docutils literal"><span class="pre">FileField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.FilePathField" title="django.db.models.FilePathField"><tt class="xref py py-class docutils literal"><span class="pre">FilePathField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.FilePathField" title="django.forms.FilePathField"><tt class="xref py py-class docutils literal"><span class="pre">FilePathField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.FloatField" title="django.db.models.FloatField"><tt class="xref py py-class docutils literal"><span class="pre">FloatField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.FloatField" title="django.forms.FloatField"><tt class="xref py py-class docutils literal"><span class="pre">FloatField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.ForeignKey" title="django.db.models.ForeignKey"><tt class="xref py py-class docutils literal"><span class="pre">ForeignKey</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.ModelChoiceField" title="django.forms.ModelChoiceField"><tt class="xref py py-class docutils literal"><span class="pre">ModelChoiceField</span></tt></a>
(see below)</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">ImageField</span></tt></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.ImageField" title="django.forms.ImageField"><tt class="xref py py-class docutils literal"><span class="pre">ImageField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.IntegerField" title="django.db.models.IntegerField"><tt class="xref py py-class docutils literal"><span class="pre">IntegerField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.IntegerField" title="django.forms.IntegerField"><tt class="xref py py-class docutils literal"><span class="pre">IntegerField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">IPAddressField</span></tt></td>
<td><tt class="docutils literal"><span class="pre">IPAddressField</span></tt></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.GenericIPAddressField" title="django.db.models.GenericIPAddressField"><tt class="xref py py-class docutils literal"><span class="pre">GenericIPAddressField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.GenericIPAddressField" title="django.forms.GenericIPAddressField"><tt class="xref py py-class docutils literal"><span class="pre">GenericIPAddressField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.ManyToManyField" title="django.db.models.ManyToManyField"><tt class="xref py py-class docutils literal"><span class="pre">ManyToManyField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.ModelMultipleChoiceField" title="django.forms.ModelMultipleChoiceField"><tt class="xref py py-class docutils literal"><span class="pre">ModelMultipleChoiceField</span></tt></a>
(see below)</td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.NullBooleanField" title="django.db.models.NullBooleanField"><tt class="xref py py-class docutils literal"><span class="pre">NullBooleanField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.CharField" title="django.forms.CharField"><tt class="xref py py-class docutils literal"><span class="pre">CharField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.PositiveIntegerField" title="django.db.models.PositiveIntegerField"><tt class="xref py py-class docutils literal"><span class="pre">PositiveIntegerField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.IntegerField" title="django.forms.IntegerField"><tt class="xref py py-class docutils literal"><span class="pre">IntegerField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.PositiveSmallIntegerField" title="django.db.models.PositiveSmallIntegerField"><tt class="xref py py-class docutils literal"><span class="pre">PositiveSmallIntegerField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.IntegerField" title="django.forms.IntegerField"><tt class="xref py py-class docutils literal"><span class="pre">IntegerField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.SlugField" title="django.db.models.SlugField"><tt class="xref py py-class docutils literal"><span class="pre">SlugField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.SlugField" title="django.forms.SlugField"><tt class="xref py py-class docutils literal"><span class="pre">SlugField</span></tt></a></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.SmallIntegerField" title="django.db.models.SmallIntegerField"><tt class="xref py py-class docutils literal"><span class="pre">SmallIntegerField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.IntegerField" title="django.forms.IntegerField"><tt class="xref py py-class docutils literal"><span class="pre">IntegerField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.TextField" title="django.db.models.TextField"><tt class="xref py py-class docutils literal"><span class="pre">TextField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.CharField" title="django.forms.CharField"><tt class="xref py py-class docutils literal"><span class="pre">CharField</span></tt></a> with
<tt class="docutils literal"><span class="pre">widget=forms.Textarea</span></tt></td>
</tr>
<tr class="row-even"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.TimeField" title="django.db.models.TimeField"><tt class="xref py py-class docutils literal"><span class="pre">TimeField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.TimeField" title="django.forms.TimeField"><tt class="xref py py-class docutils literal"><span class="pre">TimeField</span></tt></a></td>
</tr>
<tr class="row-odd"><td><a class="reference internal" href="../../../ref/models/fields/#django.db.models.URLField" title="django.db.models.URLField"><tt class="xref py py-class docutils literal"><span class="pre">URLField</span></tt></a></td>
<td><a class="reference internal" href="../../../ref/forms/fields/#django.forms.URLField" title="django.forms.URLField"><tt class="xref py py-class docutils literal"><span class="pre">URLField</span></tt></a></td>
</tr>
</tbody>
</table>