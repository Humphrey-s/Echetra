
$(document).ready(function () {

	$(".Tadd").click(function () {

		$("#aadd").css("display", "inline-block");

		/*$(".Ttasks").append(`<div id="task">
				<label id="done"><input type="checkbox">
					<span></span>
				</input></label>
			</div>`)*/
	});

	$("#aadd").keydown(function (event) {

		if (event.keyCode === 13) {
			const taskName = $(this).val()
			$(this).val('')

			$(this).css("display", "None") 
			$(".Ttasks").append(`<div id="task">
                                <label id="done"><input type="checkbox">
                                        <span></span>
                                </input></label>
				<div id="name">
					<p>${taskName}</p>
				</div>
                        </div>`)
		}
	});
});
