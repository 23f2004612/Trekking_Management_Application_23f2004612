<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-title">Trek Participants</h2>
        <p class="text-muted mb-0">View all registered participants for this trek.</p>
      </div>

      <RouterLink to="/staff/treks" class="btn btn-outline-success">
        <i class="bi bi-arrow-left me-1"></i>
        Back
      </RouterLink>
    </div>

    <SearchBar @search="searchParticipants" />

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="participants.length === 0"
      :title="searching ? 'No Matching Participants' : 'No Participants Found'"
      :message="
        searching
          ? 'Try searching with a different keyword.'
          : 'No users have booked this trek yet.'
      "
      :icon="searching ? 'bi bi-search' : 'bi bi-people'"
    />

    <div v-else class="table-card mt-4">
      <div class="table-responsive">
        <table class="table align-middle mb-0">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Contact</th>
              <th>Joined</th>
              <th>User Status</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="user in participants" :key="user.id">
              <td class="fw-semibold">
                {{ user.full_name }}
              </td>

              <td class="text-muted-cell">
                {{ user.email }}
              </td>

              <td>
                {{ user.contact_number || '-' }}
              </td>

              <td>
                {{ formatDate(user.created_at) }}
              </td>

              <td>
                <span class="badge badge-active"> Registered </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import { useRoute } from 'vue-router'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import SearchBar from '@/components/dashboard/SearchBar.vue'

import Loader from '@/components/common/Loader.vue'
import EmptyState from '@/components/common/EmptyState.vue'

import { getParticipants } from '@/services/staffService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const route = useRoute()

const loading = ref(false)

const participants = ref([])

const allParticipants = ref([])
const searching = ref(false)

async function loadParticipants() {
  loading.value = true

  try {
    const res = await getParticipants(route.params.id)
    participants.value = res.data
    allParticipants.value = [...res.data]
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load participants')
  } finally {
    loading.value = false
  }
}

function searchParticipants(value = '') {
  const q = value.toLowerCase().trim()
  searching.value = value.trim() !== ''

  if (!q) {
    participants.value = [...allParticipants.value]

    return
  }

  participants.value = allParticipants.value.filter(
    (user) =>
      user.full_name.toLowerCase().includes(q) ||
      user.email.toLowerCase().includes(q) ||
      (user.contact_number || "").toLowerCase().includes(q)
  )
}

function formatDate(date) {
  if (!date) return '-'

  return new Date(date).toLocaleDateString()
}

onMounted(loadParticipants)
</script>

<style scoped>
.table-card {
  background: white;

  border-radius: 18px;

  padding: 20px;

  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
}

.page-title {
  font-weight: 700;
}

.text-muted-cell {
  color: #777;
}

.badge {
  padding: 8px 14px;

  border-radius: 20px;

  font-weight: 600;
}

.badge-active {
  background: #dff7e8;

  color: #167347;
}

thead th {
  font-weight: 700;

  color: #555;
}
</style>
