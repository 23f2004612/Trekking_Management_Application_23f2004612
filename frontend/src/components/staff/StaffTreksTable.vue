<template>
  <div class="table-card mt-4">
    <div class="table-responsive">
      <table class="table align-middle mb-0">
        <thead>
          <tr>
            <th>Trek</th>

            <th>Location</th>

            <th>Difficulty</th>

            <th>Slots</th>

            <th>Status</th>

            <th class="text-center">Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="trek in treks" :key="trek.id">
            <td class="fw-semibold">
              {{ trek.trek_name }}
            </td>

            <td>
              {{ trek.location }}
            </td>

            <td>
              <span class="difficulty-dot" :class="difficultyDotClass(trek.difficulty)"></span>

              {{ trek.difficulty }}
            </td>

            <td>{{ trek.booked_slots }} / {{ trek.available_slots }}</td>

            <td>
              <span class="badge" :class="badgeClass(trek.status)">
                {{ trek.status }}
              </span>
            </td>

            <td class="text-center">
              <button
                class="action-icon-btn edit-btn me-2"
                @click="$emit('manage', trek)"
                :disabled="trek.status === 'Completed'"
                :title="
                  trek.status === 'Completed' ? 'Completed treks cannot be edited' : 'Manage Trek'
                "
              >
                <i class="bi bi-pencil"></i>
              </button>

              <RouterLink
                class="action-icon-btn booking-btn me-2"
                :to="`/staff/trek/${trek.id}`"
                title="Participants"
              >
                <i class="bi bi-people"></i>
              </RouterLink>

              <button
  class="action-icon-btn complete-btn"
  :disabled="trek.status === 'Completed'"
  :title="
    trek.status === 'Completed'
      ? 'Trek already completed'
      : 'Complete Trek'
  "
  @click="$emit('complete', trek)"
>
  <i class="bi bi-check2-circle"></i>
</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>

defineProps({
  treks: Array,
})

defineEmits(['manage', 'complete'])

function difficultyDotClass(difficulty) {
  switch (difficulty) {
    case 'Easy':
      return 'dot-easy'

    case 'Moderate':
      return 'dot-moderate'

    case 'Hard':
      return 'dot-hard'

    default:
      return ''
  }
}

function badgeClass(status) {
  switch (status) {
    case 'Open':
      return 'badge-active'

    case 'Closed':
      return 'badge-blacklisted'

    case 'Completed':
      return 'badge-completed'

    default:
      return 'bg-secondary'
  }
}
</script>

<style scoped>
.table-card {
  background: white;

  border-radius: 18px;

  padding: 18px;

  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
}

.text-muted-cell {
  color: #777;
}

.badge {
  padding: 8px 14px;

  font-weight: 600;

  border-radius: 20px;
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

.action-icon-btn {
  width: 40px;

  height: 40px;

  border: none;

  border-radius: 10px;

  display: inline-flex;

  justify-content: center;

  align-items: center;

  transition: 0.2s;
}

.edit-btn {
  background: #eef8f2;

  color: #184e37;
}

.booking-btn {
  background: #edf4ff;

  color: #2563eb;

  text-decoration: none;
}

.action-btn {
  border: none;

  padding: 8px 16px;

  border-radius: 10px;

  font-weight: 600;
}

.complete-btn {
  background: #5f977f;
  color: white;
}

.action-icon-btn:hover {
  transform: translateY(-2px);
}

thead th {
  font-weight: 700;
  color: #555;
}
.difficulty-dot {
  display: inline-block;

  width: 10px;

  height: 10px;

  border-radius: 50%;

  margin-right: 8px;

  vertical-align: middle;
}

.dot-easy {
  background: #28a745;
}

.dot-moderate {
  background: #f39c12;
}

.dot-hard {
  background: #dc3545;
}

.action-icon-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed !important;
  transform: none;
  filter: grayscale(40%);
}

.action-icon-btn:disabled i {
  cursor: not-allowed !important;
}
</style>
