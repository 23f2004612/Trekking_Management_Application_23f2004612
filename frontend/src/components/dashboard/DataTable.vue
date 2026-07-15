<template>
  <div class="table-card">
    <table class="table table-hover align-middle mb-0">
      <thead>
        <tr>
          <th>Name</th>
          <th>Location</th>
          <th>Difficulty</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Difficulty</th>
          <th>Assigned Staff</th>
          <th>Slots</th>
          <th>Status</th>
          <th class="text-end">Actions</th>
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

          <td class="fw-semibold">
              {{ trek.start_date }}
          </td>

          <td class="fw-semibold">
              {{ trek.end_date }}
          </td>

          <td>
            <span :class="['badge', difficultyDotClass(trek.difficulty)]">
              {{ trek.difficulty }}
            </span>
          </td>

          <td>
            {{ trek.staff?.full_name || "Not Assigned" }}
          </td>

          <td>{{ trek.booked_slots }} / {{ trek.available_slots }}</td>

          <td>
            <span :class="['badge', statusBadgeClass(trek.status)]">
              {{ trek.status }}
            </span>
          </td>

          <td class="text-end">
            <button class="icon-btn edit-btn me-2" @click="$emit('edit', trek)" title="Edit">
              <i class="bi bi-pencil"></i>
            </button>

            <button class="icon-btn delete-btn" @click="$emit('delete', trek)" title="Close Trek">
              <i class="bi bi-trash"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
defineProps({
  treks: Array,
})
defineEmits(['edit', 'delete'])

const statusBadgeClass = (status) =>
  ({
    Open: 'bg-success',
    Closed: 'bg-danger',
    completed: 'bg-secondary',
  })[status] || 'bg-warning'

const difficultyDotClass = (difficulty) =>
  ({
    Easy: 'dot-easy',
    Moderate: 'dot-moderate',
    Hard: 'dot-hard',
  })[difficulty] || 'dot-moderate'
</script>

<style scoped>
.table-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.table thead th {
  background: #faf8f3;
  color: #8a8a8a;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  padding: 16px 20px;
  border-bottom: 1px solid #ececec;
}

.table tbody td {
  padding: 16px 20px;
  color: #3b3b3b;
  border-bottom: 1px solid #f2f2f2;
  font-size: 0.92rem;
}

.table tbody tr:last-child td {
  border-bottom: none;
}

.table-hover tbody tr:hover {
  background-color: #faf8f3;
}

.difficulty-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 8px;
}

.dot-easy {
  background: #2d6a4f;
}

.dot-moderate {
  background: #d9a441;
}

.dot-hard {
  background: #c0524b;
}

.badge {
  font-weight: 600;
  font-size: 0.72rem;
  padding: 6px 12px;
  border-radius: 999px;
  text-transform: capitalize;
}

.icon-btn {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  border: 1px solid #e2e2e2;
  background: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition:
    background 0.2s ease,
    color 0.2s ease,
    border-color 0.2s ease;
}

.edit-btn {
  color: #184e37;
}

.edit-btn:hover {
  background: #edf7f0;
  border-color: #184e37;
}

.delete-btn {
  color: #c0524b;
}

.delete-btn:hover {
  background: #fbeceb;
  border-color: #c0524b;
}
</style>
