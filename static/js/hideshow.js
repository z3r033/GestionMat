$(function() {
    $('input[name="id_contrat_maintenance"]').on('click', function() {
        alert("hello")
        if ($(this).val() == 'True') {
            $('#id_duree').show();
        }
        else {
            $('#id_duree').hide();
        }
    });
})
