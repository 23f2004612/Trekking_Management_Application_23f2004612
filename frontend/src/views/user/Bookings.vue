<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-title">My Bookings</h2>
        <p class="text-muted mb-0">View your trekking history and manage bookings.</p>
      </div>

      <button class="btn btn-success" @click="exportHistory">
        <i class="bi bi-download me-2"></i>
        Export History
      </button>
    </div>

    <SearchBar @search="searchBookings" />

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="bookings.length === 0"
      :title="searching ? 'No Matching Bookings' : 'No Bookings Found'"
      :message="
        searching ? 'Try searching with another keyword.' : 'You have not booked any treks yet.'
      "
      :icon="searching ? 'bi bi-search' : 'bi bi-map'"
    />

    <BookingsTable v-else :bookings="bookings" @cancel="cancelBookingHandler" />
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import SearchBar from '@/components/dashboard/SearchBar.vue'
import Loader from '@/components/common/Loader.vue'
import EmptyState from '@/components/common/EmptyState.vue'

import BookingsTable from '@/components/user/BookingsTable.vue'

import { bookingHistory, cancelBooking, exportBookings, exportStatus } from '@/services/userService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const loading = ref(false)

const bookings = ref([])

const allBookings = ref([])

const searching = ref(false)

async function loadBookings() {
  loading.value = true

  try {
    const res = await bookingHistory()

    allBookings.value = res.data

    bookings.value = [...res.data]
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load bookings')
  } finally {
    loading.value = false
  }
}

function searchBookings(value = '') {
  searching.value = value.trim() !== ''

  if (!value.trim()) {
    bookings.value = [...allBookings.value]
    return
  }

  const q = value.toLowerCase()

  bookings.value = allBookings.value.filter(
    (booking) =>
      booking.trek.trek_name.toLowerCase().includes(q) ||
      booking.trek.location.toLowerCase().includes(q) ||
      booking.booking_status.toLowerCase().includes(q),
  )
}

async function cancelBookingHandler(id) {
  try {
    await cancelBooking(id)

    toast.success('Booking Cancelled')

    loadBookings()
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to cancel booking')
  }
}

async function exportHistory() {
  try {
    const res = await exportBookings()

    toast.success('Preparing export...')

    const taskId = res.data.task_id

    const interval = setInterval(async () => {
      try {
        const status = await exportStatus(taskId)

        if (status.data.state === 'SUCCESS') {
          clearInterval(interval)
          toast.success('Export Ready')
          window.open(
              `http://localhost:5000/api/user/download?file=${encodeURIComponent(status.data.file)}`,
              "_blank"
          )
        }

        if (status.data.state === 'FAILURE') {
          clearInterval(interval)

          toast.error('Export Failed')
        }
      } catch {
        clearInterval(interval)

        toast.error('Export Failed')
      }
    }, 1500)
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to export')
  }
}

onMounted(loadBookings)
</script>

<style scoped>
.page-title {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
}

.btn-success {
  border-radius: 10px;
}
</style>
