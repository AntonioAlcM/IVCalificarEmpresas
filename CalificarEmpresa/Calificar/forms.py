#-*- coding: utf-8 -*-
from django import forms
import urllib, json
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import InlineField

class FormCreacionEmpresa(forms.Form):
	Nombre=forms.CharField(max_length=100, help_text='100 carácteres máximo.',error_messages={'necesario': 'Introducir tu nombre'})
	AnhoCreacion=forms.IntegerField()
	Empresa_id=forms.CharField()
	def __init__(self, *args, **kwargs):
		super(FormCreacionEmpresa, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Registrar',css_class='btn btn-warning'))
		self.helper.layout = Layout(
		InlineField('Nombre', css_class='input-xlarge'),
  		InlineField('AnhoCreacion', css_class='input-xlarge'),
		InlineField('Empresa_id', css_class='input-xlarge'),)
