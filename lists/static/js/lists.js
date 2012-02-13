$(document).ready(function() {
	$('#add_item').on('click', addItem);
});

function addItem(){
	var newItem = $('new_item').val();
	$.ajaxSend()
}