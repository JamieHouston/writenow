var WriteNow = WriteNow || {};
WriteNow.UI = WriteNow.UI || {};

(function ($) {
	(function() {
		this.initListView = function(){
			$('#add_item').on('click', addItem);

			$('#clear_list').on('click', clearList);

			runOnEnter($('#new_list'), createList);

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
					$('#empty_message').fadeOut();
					$('#clear_list').show();
					$('#items').append('<label class="checkbox"><input type="checkbox" name="complete" id="' + item.pk + '"><span>' + item.name + '</span></label>');
					$('#new_item').val('');
					$('#new_item').focus();
				}
			});
		}

		function clearList(){
			$.ajax('clear/');
			$('#items').empty();
			$('#empty_message').fadeIn();
			$('#clear_list').hide();
			$('#new_item').focus();
		}

		function updateStatus(){
			var $item = $(this);
			var content = $item.next().html();
			if (content.startsWith('http')  && confirm('open link?')){
				$item.attr('checked', false);
				window.open(content);
				return false;
			}
			if ($item.is(':checked')){
				$item.parent().addClass('complete').delay(500).fadeOut();
				$.ajax('remove/' + this.id, {
					success: function(){
						if ($('#items').children.length === 0){
							$('#empty_message').fadeIn();
							$('#clear_list').hide();
						}
					}
				});
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
			var pathArray = location.pathname.split('/');
			pathArray.pop(); // remove the list name
			if (location.pathname.substr(-1) === "/"){
				pathArray.pop();
			}
			pathArray.push($('#new_list').val());
			location.href = pathArray.join('/');
		}
	}).apply(WriteNow.UI);
})(jQuery);

/**
 * jQuery.browser.mobile (http://detectmobilebrowser.com/)
 *
 * jQuery.browser.mobile will be true if the browser is a mobile device
 *
 **/
(function(a){jQuery.browser.mobile=/android.+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))})(navigator.userAgent||navigator.vendor||window.opera);

// add startswith to strings
if (typeof String.prototype.startsWith != 'function') {
  String.prototype.startsWith = function (str){
    return this.indexOf(str) == 0;
  };
}