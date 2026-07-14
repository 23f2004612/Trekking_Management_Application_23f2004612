<template>
  <div class="card shadow-sm border-0 trek-card">
    <div class="card-body">
      <div class="d-flex justify-content-between mb-3">
        <span class="badge bg-success">
          {{ trek.status }}
        </span>

        <span class="badge bg-warning text-dark">
          {{ trek.difficulty }}
        </span>
      </div>

      <h4>{{ trek.trek_name }}</h4>

      <p class="text-muted mb-2">
        <i class="bi bi-geo-alt-fill"></i>

        {{ trek.location }}
      </p>

      <p class="small text-muted">
        {{ trek.description }}
      </p>

      <div class="row mt-3">
        <div class="col">
          <small>
            <b>Duration</b>

            <br />

            {{ trek.duration }} Days
          </small>
        </div>

        <div class="col">
          <small>
            <b>Slots</b>

            <br />

            {{ trek.available_slots - trek.booked_slots }}
          </small>
        </div>
      </div>

      <hr />

      <div class="d-flex justify-content-between">
        <small>
          {{ trek.start_date }}
        </small>

        <button class="btn btn-success btn-sm">View</button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  trek: Object,
})
</script>

<style scoped>
.trek-card {
  border-radius: 18px;

  transition: 0.25s;
}

.trek-card:hover {
  transform: translateY(-6px);
}
</style>
