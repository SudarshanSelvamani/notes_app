var titeItem = $(".title")
    $("#preview-title").text(titeItem.val())

    var bodyItem = $(".body")
    

    function setcontent(value){
        var markedContent = marked(value)
        $("#preview-body").html(markedContent)
    }

    setcontent(bodyItem.val())

    bodyItem.keyup(
        function(){
            var newContent = $(this).val()
            setcontent(newContent)
        }
    )
