function select_cell(event){
    // User clicks or navigates to a cell.
    if ($(event.target).is("td")) {
        make_into_input($(event.target).children('div'));
    } else if ($(event.target).is("div")) {
        make_into_input($(event.target));
    }
}

function make_into_input(element){
    // Make text grade into input for grade entry
    value = 90;
    parent = $(element).parent('td');
    $(element).replaceWith('<input onblur="mark_change(event)" onkeydown="return keyboard_nav(event)" class="grade_input" prev_value="'+value+'" value="'+value+'"/>');
    $(parent).children('input').focus();
    $(parent).children('input').select();
}

function mark_change(event) {
    // Mark a changed grade. It will save then come back as save success.
    $prev_value = $(event.target).attr('prev_value');
    if ( $prev_value != $(event.target).val() ) {
        $(event.target).removeClass('save_success');
        $(event.target).addClass('saving');
        $.post(  
          "gradebook/ajax_save_grade/",
          function(data){
            if (data == "SUCCESS") {
                $new_value = $(event.target).val();
                $(event.target).replaceWith('<div class="save_success">' + $new_value + '</div>');
            }
          }  
        );
    } else {
        $(event.target).replaceWith('<div>' + $(event.target).val() + '</div>');
    }
    
}

function get_new_assignment_form(event){
    // Get a new assignment form to display of modal overlay
    $.post(
        "ajax_get_item_form/",
        function(data){  
            $("#new_assignment_form").html(data);
        }  
    ); 
    $("#new_assignment_form").overlay({
            top: '3',
            fixed: false
        });
    $("#new_assignment_form").overlay().load();
}

function handle_form_fragment_submit(form) {
    // Handle submit for an assignment with ajax
    form_data = $(form).serialize();
    $.post(  
        "ajax_get_item_form/",
        form_data,
        function(data){
            if ( data == "SUCCESS" ){
                alert('Great Job!');
                location.reload();
            } else {
                $("#new_assignment_form").html(data);
            }
        }  
    );
    return false;
}

function keyboard_nav(event) {
    key = event.which;
    if (key == 13 || key == 40 || key == 38 || key == 37 || key == 39) {
        column = $(event.target).parents('td').attr('id').replace(/_r\d*/, '').replace(/tdc/,'').trim();
        row = $(event.target).parents('td').attr('id').replace(/^tdc\d*_r/, '').trim();
        
        var selected_element;
        if(key == 13 || key == 40) { // Down
            selected_element = $('td#tdc' + column + '_r' + (parseInt(row)+1));
        } else if (key == 38) { // Up
            selected_element = $('td#tdc' + column + '_r' + (parseInt(row)-1));
        } else if (key == 37) { // Left
            selected_element = $('td#tdc' + (parseInt(column)-1) + '_r' + row);
        } else if (key == 39) { // Right
            selected_element = $('td#tdc' + (parseInt(column)+1) + '_r' + row);
        }
        make_into_input($(selected_element).children('div'));
        $(selected_element).children('input').focus();
        $(selected_element).children('input').select();
        return false;
    }
}