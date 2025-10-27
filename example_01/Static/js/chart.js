<script>
const ctx = document.getElementById('vendasChart').getContext('2d');
const data = {
    labels: [{% for row in vendas_por_cliente %}'{{ row['nome'] }}'{% if not loop.last %}, {% endif %}{% endfor %}],
    datasets: [{
        label: 'Total de Vendas por Cliente',
        data: [{% for row in vendas_por_cliente %}{{ row['total'] }}{% if not loop.last %}, {% endif %}{% endfor %}],
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
    }]
};
new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
        responsive: true,
        scales: {
            y: { beginAtZero: true }
        }
    }
});
</script>
