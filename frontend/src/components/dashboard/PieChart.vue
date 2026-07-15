<template>
  <div class="card shadow-sm border-0">
    <div class="card-body">
      <Pie :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

defineProps({
  chartData: Object,
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,

  plugins: {
    legend: {
      display: true,
      position: 'bottom',

      labels: {
        boxWidth: 18,
        padding: 20,
        font: {
          size: 13,
          weight: '600',
        },
      },
    },

    tooltip: {
      enabled: true,
    },
  },
}
</script>

<style scoped>
.card {
  height: 350px;
}
</style>
