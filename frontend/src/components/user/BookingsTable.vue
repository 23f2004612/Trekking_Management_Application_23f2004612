<template>
  <div class="table-card mt-4">
    <div class="table-responsive">
      <table class="table align-middle mb-0">
        <thead>
          <tr>
            <th>Trek</th>
            <th>Location</th>
            <th>Duration</th>
            <th>Booked On</th>
            <th>Status</th>
            <th class="text-center">Action</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="booking in bookings" :key="booking.id">
            <td class="fw-semibold">
              {{ booking.trek.trek_name }}
            </td>

            <td>
              {{ booking.trek.location }}
            </td>

            <td>{{ booking.trek.duration }} Days</td>

            <td>
              {{ formatDate(booking.booking_date) }}
            </td>

            <td>
              <span class="badge" :class="badgeClass(booking.booking_status)">
                {{ booking.booking_status }}
              </span>
            </td>

            <td class="text-center">
              <button
                v-if="booking.booking_status === 'Booked'"
                class="action-btn cancel-btn"
                @click="$emit('cancel', booking.id)"
              >
                <i class="bi bi-x-circle me-1"></i>

                Cancel
              </button>

              <span v-else class="text-muted"> — </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
defineProps({
  bookings: Array,
})

defineEmits(['cancel'])

function badgeClass(status) {
  switch (status) {
    case 'Booked':
      return 'badge-active'

    case 'Completed':
      return 'badge-completed'

    case 'Cancelled':
      return 'badge-blacklisted'

    default:
      return 'bg-secondary'
  }
}

function formatDate(date) {
  return new Date(date).toLocaleDateString()
}
</script>

<style scoped>
.table-card {
  background: white;

  border-radius: 18px;

  padding: 18px;

  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
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

.badge-blacklisted {
  background: #fde7e7;

  color: #c0392b;
}

.badge-completed {
  background: #ececec;

  color: #555;
}

.action-btn {
  border: none;

  border-radius: 10px;

  padding: 8px 18px;

  font-weight: 600;
}

.cancel-btn {
  background: #fde7e7;

  color: #c0392b;
}

.cancel-btn:hover {
  background: #f8d7da;
}

thead th {
  color: #555;

  font-weight: 700;
}
</style>
