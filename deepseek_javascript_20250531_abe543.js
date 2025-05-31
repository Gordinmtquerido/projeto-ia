fetch('/api/analytics')
  .then(res => res.json())
  .then(data => {
    new Chart(document.getElementById('sentiment-chart'), {
      type: 'pie',
      data: {
        labels: ['Positivo', 'Negativo'],
        datasets: [{
          data: [data.positive, data.negative],
          backgroundColor: ['#4CAF50', '#F44336']
        }]
      }
    });
  });