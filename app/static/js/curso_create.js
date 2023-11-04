$(document).ready(function() {
    $('.coordenador-item').click(function(e) {
        e.preventDefault();
        var coordenadorValue = $(this).data('value');
        var coordenadorNome = $(this).text();  // Obtém o texto do elemento clicado

        console.log(coordenadorValue, coordenadorNome);
        
        $('#coordenador-input').val(coordenadorValue);
        $('#coordenador-nome').text(coordenadorNome);
    });
    $('.periodo-item').click(function(e) {
        e.preventDefault();
        var periodoValue = $(this).data('value');
        $('#periodo-input').val(periodoValue);
    });
    $('.modalidade-item').click(function(e) {
        e.preventDefault();
        var modalidadeValue = $(this).data('value');
        $('#modalidade-input').val(modalidadeValue);
    });
});