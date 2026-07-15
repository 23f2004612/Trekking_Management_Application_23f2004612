<template>
  <div class="card shadow-sm border-0">
    <div class="card-body">
      <Line :data="chartData" :options="options" />
    </div>
  </div>
</template>

<script setup>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
  Filler,
} from 'chart.js'

import { Line } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend, Filler)

defineProps({
  chartData: Object,
})

const options = {
  responsive: true,
  maintainAspectRatio: false,

  interaction: {
    intersect: false,
    mode: 'index',
  },

  plugins: {
    legend: {
      display: true,
      position: 'top',

      labels: {
        usePointStyle: true,
        pointStyle: 'circle',
        padding: 20,
        font: {
          size: 13,
          weight: '600',
        },
      },
    },

    tooltip: {
      enabled: true,
      backgroundColor: '#184e37',
      titleColor: '#fff',
      bodyColor: '#fff',
      padding: 12,
    },
  },

  elements: {
    line: {
      tension: 0.4,
      borderWidth: 3,
    },

    point: {
      radius: 5,
      hoverRadius: 8,
      borderWidth: 2,
      backgroundColor: '#fff',
    },
  },

  scales: {
    x: {
      grid: {
        display: false,
      },

      ticks: {
        font: {
          weight: '600',
        },
      },
    },

    y: {
      beginAtZero: true,

      grid: {
        color: '#ececec',
      },

      ticks: {
        stepSize: 10,
      },
    },
  },
}
</script>

<style scoped>
.card {
  height: 350px;
  border-radius: 18px;
}
</style>
