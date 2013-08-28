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
        myFunction($('#myform')[0], '0')
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
		status.html(xhr.responseText.slice(1,-1));
        myFunction($('#myform')[0], '1')
	}
});
function myFunction(a, b){
    if (document.all || document.getElementById) {
        for (i = 0; i < a.length; i++) {
            var formElement = a.elements[i];
            if (true && b == '0') {
                formElement.disabled = true;
                }
            else if (true && b == '1') {
                formElement.disabled = false;
				}
		}
    }
}
})();