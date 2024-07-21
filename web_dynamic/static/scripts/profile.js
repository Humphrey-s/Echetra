
function delAccount() { 
	const element = document 
		.querySelector('#delete-account-window'); 
       element.classList.toggle('visible');  
} 

$(document).ready(function () {

            $(".user-user-profile-cover").click(function () {
            		const display = $("#user-user-profile").css("display");
            		if (display === "flex") {
            			setProfile();
            			$(".user-user-profile-cover").css("display", "none");
            		}
            })

		$(".fa-chevron-left").click(function () {
			$(".user-profile-form").css("display", "none")
		});

		$(".clickhere").click(function () {
			$(".user-profile-form").css("display", "flex");
		});

            $("#bar-profile").click(function () {
            		$(".user-user-profile-cover").css("display", "flex");
            })


		$("#fileUpload").click(function (event) {
			event.preventDefault()
			$("#fileInput").click()


			$("#fileInput").change(function (event) {

				let file = event.target.files[0]
				let reader = new FileReader()


						/*$.ajax({
							type: "POST",
							url: '/echetra/resource/post',
							data: JSON.stringify({"Ok": "Yes"}),
							dataType: "json",
							contentType: "application/json",
							success: function (data) {
								console.log(JSON.stringify(data));
							},
						});*/
			
				let el = $("#pi");
				el.css("border-radius", "10px 10px 10px 10px");
				el.css("margin-bottom", "20px");
				el.css("box-shadow", "1px 1px 1px 1px");

				reader.onload = function (event) {
					el.attr('width', "100%");
					el.attr("src", event.target.result);
				};

						/*let x = $("<button id='xbtn'><h2>&times</h2></button>");
				$("#posts-text-media").prepend(x)*/
				$("#xbtn").show();
				reader.readAsDataURL(file);
			});

		});

	
            $("#settings-profile").click(function () {
            	$("#user-profile-main-form").css("display", "flex");
            	$("#user-profile-account-settings").css("display", "none")
            });

            $("#settings-account").click(function () {
            	$("#user-profile-account-settings").css("display", "flex");
            	$("#user-profile-main-form").css("display", "none");
            });

            $("#profile-banner1").click(function () {
            		$("#profile-img-input").click();
            });

            $("#add-phone").click(function () {
            	$("#input-phone-number").css("display", "flex");
            });


            $(".ipnh-x").click(function () {
            	$("#input-phone-number").css("display", "none");
            });

            $(".ipnh-x1").click(function () {
            	$("#delete-account").click();
            });

            $("#interest-for-user").change(function () {
            	if ($(this).val() !== "➕") {
            		value = $(this).val();
            		interests.push(value);
            		$(this).val("");

            		$("#selected-interests").append(`<div>${value}</div>`)
            	} 

            	console.log(interests);
            });

            $("#user-profile-theform").on("change", ":input", function () {
            	$(".save-discard-cngs").css("bottom", "20px");
            });

            $("#sdc-reset").click(function () {
            	$(".save-discard-cngs").css("bottom", "-90px");
            	$(':input', '#user-profile-theform')
            		.not(':button, :submit, :reset, :hidden')
            		.val('')
            		.prop('checked', false)
            		.prop('selected', false);
            });
	

            $("#upo-community").click(function () {
            	$("#up-posts").empty();
            	$("#up-about").remove();

            	$("#up-posts").append(
            		`
            		<div id="up-community">
            			<i class="fa-solid fa-triangle-exclamation fa-beat fa-2xl" style="color: #FFD43B;"></i>
            			<span style="font-size: 13px;">Not yet Available!!! But It's being worked on by the engineers</span>
            		</div>
            		`
            		);
            });

            $("#upo-comments").click(function () {
            	$("#up-posts").empty();
            	$("#up-about").remove();

            	$("#up-posts").append(
            		`
            		<div id="up-community">
            			<i class="fa-solid fa-triangle-exclamation fa-beat fa-2xl" style="color: #FFD43B;"></i>
            			<span style="font-size: 13px;">Not yet Available!!! But It's being worked on by the engineers</span>
            		</div>
            		`
            		);
            });

            clockUpdate();
  			setInterval(clockUpdate, 1000);
 });

			function clockUpdate() {
  					let date = new Date();
  					$('.digital-clock').css({'color': '#fff', 'text-shadow': '0 0 6px #ff0'});
  					function addZero(x) {
    					if (x < 10) {
      						return x = '0' + x;
   						 } else {
     						 return x;
    					}
  			}

  			function twelveHour(x) {
    			if (x > 12) {
      				return x = x - 12;
    			} else if (x == 0) {
      				return x = 12;
    			} else {
      				return x;
    			}
  			}

			let h = addZero(twelveHour(date.getHours()));
			let m = addZero(date.getMinutes());
			let s = addZero(date.getSeconds());

			$('.digital-clock').text(h + ':' + m + ':' + s)
			}            

