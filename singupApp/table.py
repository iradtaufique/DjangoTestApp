import django_tables2 as table

from singupApp.models import Personal


class PersonalTable(table.Table):
    editable = table.LinkColumn('edit_form', verbose_name='edit')
    class Meta:
        model = Personal
        template_name = 'django_tables2/semantic.html'
        fields = ('id', 'name', 'country', 'money', 'editable')
