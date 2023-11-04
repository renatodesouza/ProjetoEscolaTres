$(document).ready(function(){
    $('.destinatario-item').click(function(e){
        e.preventDefault();
        var destinatarioValue = $(this).data('value');
        var destinatarioNome = $(this).text();
        

        console.log(destinatarioValue);
        console.log(destinatarioNome);

        $('#destinatario-input').val(destinatarioValue);
        $('#destinatario-nome').text(destinatarioNome);
    });
});


