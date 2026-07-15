<template>
  <div class="empty-state text-center py-5">
    <i :class="icon" class="empty-icon"></i>

    <h3 class="mt-3">
      {{ title }}
    </h3>

    <p v-if="message" class="text-muted mb-0">
      {{ message }}
    </p>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: 'No Data Found',
  },

  message: {
    type: String,
    default: '',
  },

  icon: {
    type: String,
    default: 'bi bi-inbox',
  },
})
</script>

<style scoped>
.empty-state {
  padding: 60px 20px;
}

.empty-icon {
  font-size: 68px;

  color: #184e37;

  opacity: 0.7;
}

h3 {
  font-weight: 700;

  color: #184e37;
}

p {
  font-size: 0.95rem;

  margin-top: 8px;
}
</style>
