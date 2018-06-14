function deleteCalenderEntry(entry){
	$(entry).parent().remove();
	var id = $(entry).data('id');
	console.log(id);

	$.ajax({
		url: 'view/delete/' + id,
		method: 'DELETE',
		beforeSend: function(xhr){
			xhr.setRequestHeader('X-CSRFToken', csrf_token)
		}
	});

}