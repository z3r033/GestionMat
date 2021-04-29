$(document).ready(function(){
    $('#id_contrat_maintenance').click(function(){

        if ($(this).val() == 'True') {
                    alert("hi")
            $('#id_duree').show();
            $('label[for="id_duree"]').show();
             $('#id_duree').prop('required',true);
             $('#id_duree').val("");
        }
        else {
            $('#id_duree').hide();
            $('#id_duree').val("0");
            $('label[for="id_duree"]').hide ();
            $('#id_duree').removeAttr('required');
        }
    });
})