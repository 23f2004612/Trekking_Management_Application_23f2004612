<template>
  <DashboardLayout>
    <div class="mb-4">
      <h2 class="fw-bold">Staff Dashboard</h2>

      <p class="text-muted">Welcome back. Here's a quick overview of your assigned treks.</p>
    </div>

    <Loader v-if="loading" />

    <div v-else class="row g-4">
      <div class="col-md-6">
        <div class="card summary-card">
          <div class="card-body">
            <small class="text-muted"> Assigned Treks </small>

            <h2>
              {{ totalTreks }}
            </h2>
          </div>
        </div>
      </div>

      <div class="col-md-6">
        <div class="card summary-card">
          <div class="card-body">
            <small class="text-muted"> Total Participants </small>

            <h2>
              {{ totalBookings }}
            </h2>
          </div>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'

import Loader from '@/components/common/Loader.vue'

import { getAssignedTreks } from '@/services/staffService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const loading = ref(false)

const treks = ref([])

const totalTreks = computed(() => treks.value.length)

const totalBookings = computed(() =>
  treks.value.reduce(
    (sum, trek) => sum + trek.booked_slots,

    0,
  ),
)

async function loadDashboard() {
  loading.value = true

  try {
    const res = await getAssignedTreks()

    treks.value = res.data
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load dashboard')
  } finally {
    loading.value = false
  }
}

onMounted(loadDashboard)
</script>
<style scoped>
.summary-card {
  border: none;

  border-radius: 18px;

  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

.summary-card h2 {
  margin-top: 10px;

  font-weight: 700;

  color: #184e37;

  font-size: 2.2rem;
}
</style>
