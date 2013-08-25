from django import forms
from django.conf import settings


class DatePickerWidget(forms.DateInput):
    class Media:
        css = {
            'all': ('http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css',)
        }
        js = (
            "http://code.jquery.com/jquery-1.9.1.js",
            "http://code.jquery.com/ui/1.10.3/jquery-ui.js",
        )

    def render(self, name, value, attrs=None):
        return str(self.media)+'''<script>
            $(function() {
                var pickerOpts = {
                    dateFormat: "yy-mm-dd",
                    showOtherMonths: true}
                $(".datepicker").datepicker(pickerOpts);
            });</script>
            <input id="id_%s" name="%s" class="datepicker" type="text" value="%s"/>'''%(name, name, value)