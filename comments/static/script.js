$(function() {
    //...your AJAX configurations would go up here, like CSRF stuff...

    $(document).on('change', "#countrylist", function(e) {
        e.preventDefault();
        console.log($(this).val());
        var url = http: //127.0.0.1:8000/add_comment/
            $.getJSON(url, { id: $(this).val() }, function(j) {
                var options = '<option value="">---??---</option>';
                for (var i = 0; i < j.length; i++) {
                    options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['city_name'] + '</option>';
                }
                console.log(options); //This should show the new listing of filtered options.
                $("#citylist").html(options);
                $("#citylist option:first").attr('selected', 'selected');
            });
        $("#countrylist").attr('selected', 'selected');
    });

});