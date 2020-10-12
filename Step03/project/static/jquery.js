$(document).ready(function(){
    $(".btnLearnMore").click(function(e){
        console.log("hiding main div → showing Learn More div");
        $("#maindiv").hide();
        $("#learnmorediv").show();

        var id = $(this).data("id");
        console.log("ad id = " + id);
        $.ajax({
            url: '/learnmore/' + id,
            data: id,
            type: 'POST',
            success: function(response){
                $("#learnmoredatabase").empty();
                $("#learnmoredatabase").append(response);
            },
            error: function(error){
                console.log(error);
			}
		});
    });

    $("#btnretour").click(function(e){
        console.log("hiding Learn More div → showing main div");
        $("#maindiv").show();
        $("#learnmorediv").hide();
    });
});