$(function(){
	'use strict';

	var lunchVoteBtns = $('.lunch-day-item__vote-button');

	lunchVoteBtns.on('click', function(e){
		var t = $(this),
			item_id = t.attr('data-id'),
			sib = t.siblings('.lunch-day-item__vote-count');

		if(localStorage.getItem(item_id)) {
			return false;
		}

		localStorage.setItem(item_id, 1);
		t.attr('data-clicked', 1);
		sib.attr('data-clicked', 1);
		sib.text(parseInt(sib.text(), 10) + 1);

		$.ajax({
			method: "GET",
			url: "/vote/",
			data: {
				item_id: item_id
			}
		});
	});

	lunchVoteBtns.each(function(){
		var t = $(this),
			item_id = t.attr('data-id'),
			sib = t.siblings('.lunch-day-item__vote-count');

		if(localStorage.getItem(item_id)) {
			localStorage.setItem(item_id, 1);
			t.attr('data-clicked', 1);
			sib.attr('data-clicked', 1);
		}
	});
});