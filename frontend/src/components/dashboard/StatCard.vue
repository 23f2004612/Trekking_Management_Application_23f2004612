<template>
  <div class="card shadow-sm border-0 stat-card">
    <div class="card-body d-flex align-items-center gap-3">
      <div class="icon-circle" :style="{ background: color + '1a', color: color }">
        <i :class="icon"></i>
      </div>

      <div>
        <p class="stat-title">{{ title }}</p>
        <h2 class="stat-value">{{ value }}</h2>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  value: [String, Number],
  icon: { type: String, default: 'bi bi-bar-chart' },
  color: { type: String, default: '#184E37' },
})
</script>

<style scoped>
.stat-card {
  border-radius: 16px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08) !important;
}

.icon-circle {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  flex-shrink: 0;
}

.stat-title {
  color: #8a8a8a;
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.stat-value {
  font-weight: 700;
  color: #222;
  margin-bottom: 0;
}
</style>