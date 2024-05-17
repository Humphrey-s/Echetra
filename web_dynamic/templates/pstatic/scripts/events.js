$(document).ready(function () {

	$("#Hcalender").click(function () {
		if ($(".Mcalender").css("display")  === "none") {
			$(".Mcalender").css("display", "inline-block");
			

			$(".Mboard").css("display", "none")
			$(".MTodo").css("display", "none")
			$(".Mgantt").css("display", "none")
			$(".MTasks").css("display", "none")
		}
	});

	$("#Hboard").click(function () {
		if ($(".Mboard").css("display")  === "none") {
			$(".Mboard").css("display", "inline-block")
			
			$(".Mcalender").css("display", "none")
			$(".MTodo").css("display", "none")
                        $(".Mgantt").css("display", "none")
                        $(".MTasks").css("display", "none")
		}
        });

	$("#HTodo").click(function () {
                $(".MTodo").css("display", "block")
 
		$(".Mcalender").css("display", "none")
                $(".Mgantt").css("display", "none")
                $(".MTasks").css("display", "none")
		$(".Mboard").css("display", "none")
	});

	$("#Hgantt").click(function () {
                $(".Mgantt").css("display", "block")
   
                $(".Mcalender").css("display", "none")
                $(".Mboard").css("display", "none")
                $(".MTodo").css("display", "none")
                $(".MTasks").css("display", "none")
        });

	$("#Htasks").click(function () {
                $(".MTasks").css("display", "inline-block")

                $(".Mcalender").css("display", "none")
		$(".Mboard").css("display", "none")
		$(".MTodo").css("display", "none")
                $(".Mgantt").css("display", "none")
        });


	$("#Hcalender").hover(function () {
		$("#Cidentifier").css("display", "inline-block")
	},function () {
		$("#Cidentifier").css("display", "none");
	});

	$("#Hboard").hover(function () {
                $("#Bidentifier").css("display", "inline-block")
        },function () {
                $("#Bidentifier").css("display", "none");
        });

	$("#HTodo").hover(function () {
                $("#TDidentifier").css("display", "inline-block")
        },function () {
                $("#TDidentifier").css("display", "none");
        });

	$("#Htasks").hover(function () {
                $("#Tidentifier").css("display", "inline-block")
        },function () {
                $("#Tidentifier").css("display", "none");
        });

	$("#Hgantt").hover(function () {
                $("#Gidentifier").css("display", "inline-block")
        },function () {
                $("#Gidentifier").css("display", "none");
        });


});
