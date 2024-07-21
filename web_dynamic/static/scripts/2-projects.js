$(document).ready( function () {

	$("#Hcurrent").click(function () {

		$(".mainhome").empty()
		$.ajax({
			type: "GET",
			url: `http://localhost:5001/users/projects/${userid}`,
			dataType: 'json',
			success: function (data) {
				if (!data) {
					return;
				}
				else {
					$.each(data, function (i, obj) {

						if (obj.category === "webDevelopment") {
							obj.category = "web";
						}
						$(".mainhome").append(
							`
							<div id="cp">
								<div id="cpimg">
									<img src="../static/images/web/web1.png" width="400px" height="200px"></img>
								</div>
								<div id=cpwrap>
									<i id="bolt1" class="fa-solid fa-bolt" style="color: #f2c218;"></i>

									<h3><i class="objname">${obj.name}</i></h3>
									<i id="bolt2" class="fa-solid fa-bolt" style="color: #f2c218;"></i>
									<div id="objType">
										<i class="fa-solid fa-guitar" style="color: #d41125;"></i>
										<i>${obj.category}</i>
									</div>
									<div id="objDone">
										<img src="../static/images/bowling.png" width="20px" height="20px"></img>
										<i>0/100<i>
									</div>
									<div id="objDue">
										<img src="../static/images/clock.png" width="20px" height="20px"></img>
										<i>24th April</i>
									</div>
								<div>
							</div>
							`
						)
					});
				}
			}
		});
	});

	$("#Finished").click(function () {
		$(".mainhome").empty()
		$.ajax({
			type: "GET",
			url: `http://localhost:5001/users/projects/${userid}`,
			dataType: 'json',
			success: function (data) {
				if (!data) { 
					return;
				} else {
					let complete = 0
					$.each(data, function (i, obj) {

						if (!obj.complete) {
							complete = 0;
						}
						else {
							complete += 1
							`
							<div id="cp">                                                                                                                   <div id="cpimg">                                                                                                                <img src="../static/images/web/web1.png" width="400px" height="200px"></img>                                                                                                                                                            </div>                                                                                                                  <div id=cpwrap>                                                                                                                 <i id="bolt1" class="fa-solid fa-bolt" style="color: #f2c218;"></i>                                                                                                                                                                                                                                                                                                     <h3><i class="objname">${obj.name}</i></h3>                                                                             <i id="bolt2" class="fa-solid fa-bolt" style="color: #f2c218;"></i>                                                                                                                                                                             <div id="objType">                                                                                                              <i class="fa-solid fa-guitar" style="color: #d41125;"></i>                                                                                                                                                                                      <i>${obj.category}</i>                                                                                          </div>                                                                                                                  <div id="objDone">                                                                                                              <img src="../static/images/bowling.png" width="20px" height="20px"></img>                                                                                                                                                                       <i>0/100<i>                                                                                                     </div>
									<div id="objDue">
										<img src="../static/images/clock.png" width="20px" height="20px"></img>
									<i>24th April</i>
								</div>
							</div>`
						}
					});
					if (complete == 0)
					{
						$(".mainhome").append(
							`
							<div id="AllIncomplete">
								<p>No project completed</p>
							</div>
							`
						)
					}
				}
			}
		});
	});

	$("#Hstudy").click(function () {
		$(".mainhome").empty()
		$(".mainhome").append(
			`
			<div id="AllIncomplete">
                                 <p>Feature Not Yet Available</p>
                        </div>
                        `
		)
	});
});
