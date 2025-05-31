document.addEventListener('DOMContentLoaded', function() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const textInput = document.getElementById('textInput');
    const resultContainer = document.getElementById('resultContainer');
    const sentimentResult = document.getElementById('sentimentResult');
    const keywordsResult = document.getElementById('keywordsResult');
    const topicsResult = document.getElementById('topicsResult');
    const wordCount = document.getElementById('wordCount');
    const charCount = document.getElementById('charCount');
    const sentimentScore = document.getElementById('sentimentScore');

    analyzeBtn.addEventListener('click', analyzeText);

    // Função principal de análise
    async function analyzeText() {
        const text = textInput.value.trim();
        
        if (!text) {
            alert('Por favor, digite algum texto para análise');
            return;
        }
        
        // Mostrar estado de carregamento
        analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analisando...';
        analyzeBtn.disabled = true;
        
        try {
            // Simulação de análise - substituir por chamada real à API
            const analysisResults = simulateAnalysis(text);
            
            // Exibir resultados
            displayResults(analysisResults);
            resultContainer.style.display = 'block';
            
        } catch (error) {
            console.error('Erro na análise:', error);
            alert('Ocorreu um erro ao analisar o texto');
        } finally {
            // Restaurar botão
            analyzeBtn.innerHTML = '<i class="fas fa-magic"></i> Analisar';
            analyzeBtn.disabled = false;
        }
    }

    // Função de simulação (substituir por chamada real à API)
    function simulateAnalysis(text) {
        // Análise básica do texto
        const words = text.split(/\s+/).filter(word => word.length > 0);
        const characters = text.length;
        
        // Simular sentimento (0 a 1)
        const randomSentiment = Math.random();
        let sentiment;
        let sentimentIcon;
        
        if (randomSentiment > 0.6) {
            sentiment = 'Positivo';
            sentimentIcon = '<i class="fas fa-smile"></i>';
        } else if (randomSentiment < 0.4) {
            sentiment = 'Negativo';
            sentimentIcon = '<i class="fas fa-frown"></i>';
        } else {
            sentiment = 'Neutro';
            sentimentIcon = '<i class="fas fa-meh"></i>';
        }
        
        // Simular palavras-chave (as 3 palavras mais longas)
        const keywords = [...words]
            .sort((a, b) => b.length - a.length)
            .slice(0, 3)
            .map(word => word.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, ''))
            .filter(word => word.length > 3);
        
        // Simular tópicos (categorias fictícias)
        const possibleTopics = ['Administração', 'Finanças', 'Processos', 'Gestão', 'Logística'];
        const topics = possibleTopics
            .sort(() => 0.5 - Math.random())
            .slice(0, 2);
        
        return {
            text,
            wordCount: words.length,
            charCount: characters,
            sentiment,
            sentimentScore: randomSentiment,
            sentimentIcon,
            keywords,
            topics
        };
    }

    // Exibir resultados na interface
    function displayResults(results) {
        // Atualizar métricas básicas
        wordCount.textContent = results.wordCount;
        charCount.textContent = results.charCount;
        sentimentScore.textContent = results.sentimentScore.toFixed(2);
        
        // Atualizar sentimento
        sentiment