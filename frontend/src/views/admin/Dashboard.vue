<template>
  <DashboardLayout>
    <div class="row g-4 mb-4">
      <div class="col-md-3">
        <StatCard title="Treks" :value="summary.total_treks" icon="bi bi-signpost-split" color="#184E37" />
      </div>

      <div class="col-md-3">
        <StatCard title="Users" :value="summary.total_users" icon="bi bi-people" color="#2D6A4F" />
      </div>

      <div class="col-md-3">
        <StatCard title="Staff" :value="summary.total_staff" icon="bi bi-person-badge" color="#B08968" />
      </div>

      <div class="col-md-3">
        <StatCard title="Bookings" :value="summary.total_bookings" icon="bi bi-calendar-check" color="#3B6E8F" />
      </div>
    </div>

    <div class="row g-4">
      <div class="col-lg-8">
        <div class="card border-0 shadow-sm chart-card">
          <div class="card-body">
            <h5 class="chart-title mb-3">Bookings Trend</h5>
            <LineChart :chartData="lineData" />
          </div>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="card border-0 shadow-sm chart-card">
          <div class="card-body">
            <h5 class="chart-title mb-3">Trek Difficulty</h5>
            <PieChart :chartData="pieData" />
          </div>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import StatCard from '@/components/dashboard/StatCard.vue'
import LineChart from '@/components/dashboard/LineChart.vue'
import PieChart from '@/components/dashboard/PieChart.vue'

import { getDashboard } from '@/services/adminService'

const summary = reactive({
  total_treks: 0,
  total_users: 0,
  total_staff: 0,
  total_bookings: 0,
})

const pieData = reactive({
  labels: [],

  datasets: [
    {
      data: [],

      backgroundColor: [
        "#4CAF50",
        "#FFC107",
        "#F44336",
      ],

      borderColor: "#ffffff",

      borderWidth: 2,

      hoverOffset: 12,
    },
  ],
});

const lineData = reactive({
  labels: [],

  datasets: [
    {
      label: "Bookings",

      data: [],

      borderColor: "#184e37",

      backgroundColor: "rgba(24,78,55,0.15)",

      fill: true,

      pointBackgroundColor: "#184e37",

      pointBorderColor: "#ffffff",
    },
  ],
});

async function loadSummary() {
  try {

    const res = await getDashboard()
    summary.total_treks = res.data.total_treks
    summary.total_users = res.data.total_users
    summary.total_staff = res.data.total_staff
    summary.total_bookings = res.data.total_bookings

    lineData.labels = Object.keys(res.data.monthly_bookings);
    lineData.datasets[0].data = Object.values(res.data.monthly_bookings);

    pieData.labels = Object.keys(res.data.difficulty_distribution);
    pieData.datasets[0].data = Object.values(res.data.difficulty_distribution);
  } catch (err) {
    console.error(err)
  }
}

onMounted(loadSummary)
</script>

<style scoped>
.chart-card {
  border-radius: 16px;
}

.chart-title {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
  color: #222;
}
</style>