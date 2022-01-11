$(document).ready(function() {
    $('#draw, #redraw').on('click', function () {
        let prize_id = $('#prize_id :selected').val();
        $('#person').text("");
        $.ajax({
            url: '/draw/ajax/getaward/',
            method:'GET',
            data: {
                prize_id: prize_id,
            },
            success: function (res){
                $('#person').text(res.person_name);
                $('#id_emp').val(res.person_id);
                $('#id_prize').val(prize_id);
            },
        });
    });
    $(document).on('change', '#prize_id', function (){
        let prize_id = $('#prize_id :selected').val();
        $.ajax({
            url: '/draw/ajax/getprizestatus/',
            method:'GET',
            data: {
                prize_id: prize_id,
            },
            success: function (res){
                let prize_remain = res.prize_remain
                if (prize_remain===0){
                    $('#draw, #redraw').prop('disabled', true)
                }else{
                    $('#draw, #redraw').prop('disabled', false)
                }
                $('#prize_name').text(res.prize_name);
                $('#prize_remain').text(res.prize_remain);
            },
        });
    });
});