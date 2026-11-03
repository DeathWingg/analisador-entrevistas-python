let selectionData = null;

document.getElementById('texto-entrevista').addEventListener('mouseup', function(e) {
    const selection = window.getSelection();
    
    // Se o usuário selecionou algum texto
    if (selection.toString().trim().length > 0) {
        const range = selection.getRangeAt(0);
        
        // Truque para calcular a posição exata do texto selecionado dentro da div
        const preSelectionRange = range.cloneRange();
        preSelectionRange.selectNodeContents(this);
        preSelectionRange.setEnd(range.startContainer, range.startOffset);
        
        const start = preSelectionRange.toString().length;
        const end = start + selection.toString().length;

        // Garante que o início é sempre menor que o fim
        const minPos = Math.min(start, end);
        const maxPos = Math.max(start, end);

        selectionData = {
            inicio: minPos,
            fim: maxPos,
            texto: selection.toString()
        };

        // Posiciona o popup perto do mouse
        const popup = document.getElementById('popup-codigo');
        popup.style.top = (e.pageY + 10) + 'px';
        popup.style.left = (e.pageX + 10) + 'px';
        popup.classList.remove('hidden'); // Mostra o popup
        
    } else {
        // Se clicou sem selecionar nada, esconde o popup
        document.getElementById('popup-codigo').classList.add('hidden');
    }
});

function salvarTrecho() {
    const idEntrevista = document.getElementById('texto-entrevista').getAttribute('data-id');
    const idCodigo = document.getElementById('select-codigo').value;

    if (!selectionData || !idCodigo) return;

    const payload = {
        id_entrevista: idEntrevista,
        id_codigo: idCodigo,
        texto: selectionData.texto,
        inicio: selectionData.inicio,
        fim: selectionData.fim
    };

    // Envia os dados via Fetch API para o Python
    fetch('/salvar_trecho', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if(response.ok) {
            alert('Trecho codificado com sucesso!');
            document.getElementById('popup-codigo').classList.add('hidden');
            window.getSelection().removeAllRanges(); // Limpa a seleção azul
        } else {
            alert('Erro ao salvar o trecho.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro de conexão com o servidor.');
    });
}