
$(document).ready(function () {

	function getTasks () {

		$.ajax({
			type: "GET",
			url: `http://localhost:5001/projects/tasks/${projectId}`,
			dataType: 'json',
			contentType: 'application/json',
			success: function (tasks) {
				tasks.forEach(function (task) {
					$(".Ttasks").append(`<div id="task">
						<label class="done" id="done"><input class="completed" type="checkbox" name="${task.id}"><span></span></input></label>
						<div id="name">
							<p>${task.name}</p>
						</div>
					</div>`)
				});
			}
		});
	}

	getTasks();
	$(".downAdd").keydown(function (event) {

		if (event.keyCode === 13) {
			const taskName = $(this).val()
			$(this).val('')

			if (taskName == '') {
				$(this).attr("placeholder", "Enter New Task")
			} else {
				$.ajax({
                                type: "POST",
                                url: `http://localhost:5001/createTask`,
                                data: JSON.stringify({'taskName': taskName, 'pid': projectId}),
                                dataType: 'json',
                                contentType: 'application/json',
                                success: function(data) {
                                        const taskId = data.id
					$(".Ttasks").append(`<div id="task">
                               			 <label class="done" id="done"><input class="completed" type="checkbox" name="${taskId}"><span></span></input></label>
						<div id="name">
							<p>${taskName}</p>
						</div>
						</div>`)
				}
				});
			}
		}
	});

	$(".Ttasks").on("click", ".completed", function () {

		if (!$(this).prop("checked")) {
			const taskId = $(this).attr("name");
			$.ajax({
				type: "PUT",
				url: `http://localhost:5001/updateTask/${taskId}`,
				data: JSON.stringify({"complete": "None"}),
				dataType: 'json',
				contentType: 'application/json',
				success: function(data) {
					return;
				}
			});
		
		} else {
			const taskId = $(this).attr("name");
			$.ajax({
				type: "PUT",
				url: `http://localhost:5001/updateTask/${taskId}`,
				data: JSON.stringify({"complete": "100%"}),
				dataType: 'json',
				contentType: 'application/json',
				success: function(data) {
					return;
				}
			});
		}
	});

	$("#placeHold").click(function () {
		$(".AddTButton").css("display", "None");
		$(".AddInput").css("display", "block");
	});

	$("#circleplus2").click(function () {
		const tName = $(".downAdd").val();

		if (tName == '') {
			$(".downAdd").attr("placeholder", "Enter New Task")
		}
		else {
			$(".downAdd").val("");
			$.ajax({
				type: "POST",
				url: `http://localhost:5001/createTask`,
				data: JSON.stringify({'taskName': tName, 'pid': projectId}),
				dataType: 'json',
				contentType: 'application/json',
				success: function(data) {
					const taskId = data.id
					$(".Ttasks").append(`<div id="task">                                                                                             <label class="done" id="done"><input class="completed" type="checkbox" name="${taskId}"><span></span></input></label>
                                                <div id="name">
                                                        <p>${tName}</p>
                                                </div>
                                                </div>`)
				}
			});
		}
	});
});
