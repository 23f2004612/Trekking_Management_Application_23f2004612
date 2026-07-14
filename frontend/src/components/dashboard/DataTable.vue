<template>
  <table class="table table-hover align-middle">
    <thead>
      <tr>
        <th>Name</th>

        <th>Location</th>

        <th>Difficulty</th>

        <th>Duration</th>

        <th>Slots</th>

        <th>Status</th>

        <th>Staff</th>

        <th></th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="trek in treks" :key="trek.id">
        <td>{{ trek.trek_name }}</td>

        <td>{{ trek.location }}</td>

        <td>{{ trek.difficulty }}</td>

        <td>{{ trek.duration }} Days</td>

        <td>
          {{ trek.booked_slots }}

          /

          {{ trek.available_slots }}
        </td>

        <td>
          <span :class="['badge', statusBadgeClass(trek.status)]">
            {{ trek.status }}
          </span>
        </td>

        <td>
          {{ trek.assigned_staff?.full_name || 'Not Assigned' }}
        </td>

        <td>
          <button
            class="btn btn-warning btn-sm me-2"
            @click="$emit('edit', trek)"
            data-bs-toggle="modal"
            data-bs-target="#trekModal"
          >
            Edit
          </button>

          <button class="btn btn-danger btn-sm" @click="$emit('delete', trek)">Close</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
    defineProps({
    treks: Array,
    })
    defineEmits(['edit', 'delete'])

    const statusBadgeClass = (status) =>
    ({
        active: 'bg-success',
        cancelled: 'bg-danger',
        completed: 'bg-secondary',
    })[status] || 'bg-warning'
</script>
