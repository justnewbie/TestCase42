(function() {

var bar = $('.barC');
var percent = $('.percentC');
var status = $('#statusC');

$('form').ajaxForm({
    beforeSend: function() {
        status.empty();
        var percentVal = '0%';
        bar.width(percentVal)
        percent.html(percentVal);
    },
    uploadProgress: function(event, position, total, percentComplete) {
        var percentVal = percentComplete + '%';
        bar.width(percentVal)
        percent.html(percentVal);
    },
    success: function() {
        var percentVal = '100%';
        bar.width(percentVal)
        percent.html(percentVal);
    },
	complete: function(xhr) {
		status.html(xhr.responseText);
	},


}); $('#myform').submit(function() {
        if (document.all || document.getElementById)
        {
        for (i = 0; i < this.length; i++) {
			var formElement = this.elements[i];
				if (true) {
					formElement.disabled = true;
				}
			}
        }});
})();