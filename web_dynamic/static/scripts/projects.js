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
		/*$("#cypro").css("display", "None");
		$("#var1").val(pname);
		$("#var2").val(pcategory);
		$("#pdatantes").submit();*/

		$.ajax({
			type: "POST",
			url: "http://localhost:5001/create9project",
			data: JSON.stringify({"name": pname, "category": pcategory}),
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
		$("#projects").empty();

		$("#projects").append(
			`<section class='home'>
				<h1>Home</h1><br>
                                <div id='Hcurrent'>
                                         <h2>Current Projects</h2>
                                 </div>
                                 <div id='Finished'>
                                         <h2>Finished</h2>
                                 </div>
                                 <div id='Hstudy'>
                                         <h2>Study Rooms</h2>
                                 </div>
                         </section>`
		)
	})

	$("#project").click(function () {
		$("#projects").empty();
		$("#projects").append(
			`<section class="project">
                                        <div id="board">
						<h3>projects</h3>
                                        </div>
					<div id="Sboard">
						<input type='text' placeholder="Type/Search ..."></input>
						<i class="fa-solid fa-magnifying-glass"></i>
					</div>
                         </section>
			`
		)
		$(".project").css("display", "block")
	})

	$("#community").click(function () {
                $("#projects").empty();
		$("#projects").append(
			`<section class="community">
				<div id="commune"> 
				</div>
			`
		)
		$(".community").css("display", "block")
        })

	$("#studyroom").click(function () {
                $("#projects").empty()
		$("#projects").append(
                        `<section class="studyroom">

			</section>
                        `
                )
                $(".studyroom").css("display", "block")
        })

	$("#chess").click(function () {
                $("#projects").empty()
		$("#projects").append(
                        `<section class="chess">

                        </section>
                        `
                )
                $(".chess").css("display", "block")
        })
	$("#profile").click(function () {
                $("#projects").empty()
		$("#projects").append(
                        `<section class="profile">

                        </section>
                        `
                )
                $(".profile").css("display", "block")
        })
	$("#settings").click(function () {
                $("#projects").empty()
		$("#projects").append(
                        `<section class="settings">

                        </section>
                        `
                )
                $(".settings").css("display", "block")
        })
});
