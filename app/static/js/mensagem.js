function abrirModalMensagem(assunto, remetente, mensagem, data_envio){
    var modal = document.getElementById('modalMensagem');
    modal.style.display = 'block';

    var assuntoElement = document.getElementById('idAssunto');
    var remetenteElement = document.getElementById('idRemetente');
    var mensagemElement = document.getElementById('idMensagem');
    var dataElement = document.getElementById('idData');

    assuntoElement.textContent = "Assunto: " + assunto;
    remetenteElement.textContent = 'Enviado por: ' + remetente;
    mensagemElement.value = mensagem;
    dataElement.textContent = 'Enviado em: ' + data_envio;

    

}

function fecharModalMensagem(){
    var modal = document.getElementById('modalMensagem');
    modal.style.display = 'none';
}