$(document).ready(function () {

	$(".cbtn").click(function () {
		$("#cypro").css("display", "block")
	});

	$("#x").click(function () {
		$("#cypro").css("display", "None")
	});

	$("#Tm").click(function () {
		$(".pname").slideToggle();
		return false
	});


	$("#bcreate").click(function () {

		const pname = $("#NewPname").val();
		const pcategory = $("input[name='pcategory']:checked").val();
		if (!pname){
			const pname = "untitled"
		}
		$.ajax({
			type: "POST",
			url: "http://localhost:5001/create9project",
			data: JSON.stringify({"name": pname, "category": pcategory, "user_id": userid}),
			dataType: "json",
			contentType: "application/json",
			success: function (result) {
				console.log(result.id)
				$("#var1").val(result.id);
				$("#var2").val(result.name);
				$("#pdatantes").submit();
			}
		});

	});

	$("#dashboard").click(function () {

		$('#projects').contents().filter(function () {
			return $(this).class === "home";
		}).css("display", "block")
		$(".home").css("display", "block");
	})

	$("#project").click(function () {
		$('#projects').contents().filter(function () {
			return $(this).class !== "project";
		}).css("display", "None")
		$(".project").css("display", "block");

		$.ajax({
			type: "GET",
			url: `http://localhost:5001/users/projects/${userid}`,
			dataType: 'json',
			success: function (data) {
				console.log(data)
			}
		})

	})

	$("#community").click(function () {
                $('#projects').contents().filter(function () {
                        return $(this).class !== "community";
                }).css("display", "None")
		$(".community").css("display", "block")
        })

	$("#studyroom").click(function () {
                $('#projects').contents().filter(function () {
                        return $(this).class !== "studyroom";
                }).css("display", "None")
                $(".studyroom").css("display", "block")
        })

	$("#chess").click(function () {
                $('#projects').contents().filter(function () {
                        return $(this).class !== "chess";
                }).css("display", "None")
                $(".chess").css("display", "block")
        })
	$("#profile").click(function () {
		$('#projects').contents().filter(function () {
                        return $(this).class !== "profile";
                }).css("display", "None")
                $(".profile").css("display", "block")
        })

	$("#settings").click(function () {
                $('#projects').contents().filter(function () {
                        return $(this).class !== "settings";
                }).css("display", "None")
                $(".settings").css("display", "block")
        })
});
