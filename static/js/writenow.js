var WriteNow = WriteNow || {};
WriteNow.UI = WriteNow.UI || {};

(function ($) {
	(function() {
		this.initListView = function(){
			$('#add_item').on('click', addItem);

			$('#clear_list').on('click', clearList);

			$('body').on('change', 'input[type=checkbox]', updateStatus);

			$newItem = $('#new_item');

			runOnEnter($newItem, addItem);

			$newItem.focus();

			$('#items').sortable({
				update: updateItemSort
			});
			$('#choose_list').on('change', switchList);
		};

		this.initUserView = function(){
			$('#create_list').on('click', createList);

			runOnEnter($('#new_list'), createList);
			$('td.link_row').on('click', function(){
				window.location = $(this).children('a')[0].href;
			});
		};

		function updateItemSort(){}

		function addItem(){
			var newItem = $('#new_item').val();
			$.ajax('add/' + newItem, {
				success: function(data){
					item = JSON.parse(data);
					$('#items').append('<label class="checkbox"><input type="checkbox" name="complete" id="' + item.pk + '">' + item.name + '</label>');
					$('#new_item').val('');
					$('#new_item').focus();
				}
			});
		}

		function clearList(){
			$.ajax('clear/');
			$('#items').empty();
			$('#new_item').focus();
		}

		function updateStatus(){
			var $item = $(this);
			if ($item.is(':checked')){
				$item.parent().addClass('complete').delay(500).fadeOut();
				$.ajax('remove/' + this.id);
			}
			else {
				$item.parent().removeClass('complete');
			}

			$('#new_item').focus();
		}

		function switchList(){
			var url = $('#choose_list').val();
			if (url && url.length){
				location.href = url;
			}
		}

		function createList(){
			location.href = "/{{ user.username }}/" + $('#new_list').val();
		}
	}).apply(WriteNow.UI);
})(jQuery);