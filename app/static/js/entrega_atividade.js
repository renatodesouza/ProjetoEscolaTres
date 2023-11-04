function abrirModal(titulo, descricao, professor_id, atividade_id, professor, aluno_id) {
    // Abra o modal
  var modal = document.getElementById('id01');
  modal.style.display = 'block';

  // Atualize os detalhes da atividade no modal com as informações passadas
  var tituloElement = document.getElementById('modalTitulo');
  var descricaoElement = document.getElementById('modalDescricao');

  var professorId = document.getElementById('IdProfessor');
  var professorNome = document.getElementById('NomeProfessor');
  var atividadeInput = document.getElementById('Atividade');
  var alunoId = document.getElementById('IdAluno');

  

  // Atualize o conteúdo dos elementos com os dados da atividade
  tituloElement.textContent = "Atividade: " + titulo;
  descricaoElement.textContent = "Descrição: " + descricao;
  professorId.value = professor_id;
  professorNome.textContent = 'Professor: ' + professor;
  atividadeInput.value = atividade_id;
  alunoId.value = aluno_id;

  
}

function fecharModal() {
    // Feche o modal
    var modal = document.getElementById('id01');
    modal.style.display = 'none';
}

function exibirDataAtual() {
      var dataAtualElement = document.getElementById("data-atual");
      var dataAtualIdElement = document.getElementById("IdDataAtual");
      var dataAtual = new Date();
      var dataFormatada = dataAtual.toLocaleDateString();
      dataAtualElement.innerHTML = dataFormatada;
      dataAtualIdElement.value = dataFormatada;
  }

    // Chamar a função para exibir a data atual
    exibirDataAtual();

  $(document).ready(function(){
    $('.professor-item').click(function(e){
      e.preventDefault();

      var professorValue = $(this).data('value');
      var professorNome = $(this).text();

      $('#professor-input').val(professorValue);
      $('#professor-nome').text(professorNome);
    });
  });