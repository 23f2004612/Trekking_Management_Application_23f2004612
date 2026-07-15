<template>
  <div class="trek-card">
    <div class="card-top">
      <span class="difficulty-badge" :class="difficultyClass">
        {{ trek.difficulty }}
      </span>
      <span class="status-badge" :class="trek.status === 'Open' ? 'status-open' : 'status-closed'">
        {{ trek.status }}
      </span>
    </div>

    <h4 class="trek-name">{{ trek.trek_name }}</h4>

    <p class="trek-location">
      <i class="bi bi-geo-alt me-1"></i>
      {{ trek.location }}
    </p>

    <div class="trek-meta">
      <div class="meta-item">
        <i class="bi bi-calendar3"></i>
        <span>{{ trek.duration }} Days</span>
      </div>
      <div class="meta-item">
        <i class="bi bi-people"></i>
        <span>{{ trek.available_slots - trek.booked_slots }} slots left</span>
      </div>
    </div>

    <div class="trek-dates">
      {{ formatDate(trek.start_date) }} – {{ formatDate(trek.end_date) }}
    </div>

    <div class="trek-footer">
      <div class="staff-tag" v-if="trek.staff">
        <i class="bi bi-person-badge me-1"></i>
        {{ trek.staff.full_name }}
      </div>

      <button
        class="btn-book"
        :disabled="trek.status !== 'Open' || trek.available_slots - trek.booked_slots <= 0"
        @click="$emit('book', trek.id)"
      >
        Book Now
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  trek: Object,
})

defineEmits(['book'])

const difficultyClass = computed(() =>
  ({
    Easy: 'diff-easy',
    Moderate: 'diff-moderate',
    Hard: 'diff-hard',
  })[props.trek.difficulty] || 'diff-moderate',
)

function formatDate(dateStr) {
  if (!dateStr) return ''
  return new Date(dateStr).toLocaleDateString('en-GB', {
    day: 'numeric',
    month: 'short',
  })
}
</script>

<style scoped>
.trek-card {
  background: #fff;
  border-radius: 16px;
  padding: 22px;
  height: 100%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
}

.trek-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
}

.card-top {
  display: flex;
  justify-content: space-between;
  margin-bottom: 14px;
}

.difficulty-badge,
.status-badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 5px 12px;
  border-radius: 999px;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.diff-easy {
  background: #edf7f0;
  color: #184e37;
}

.diff-moderate {
  background: #fbf1de;
  color: #a9762e;
}

.diff-hard {
  background: #fbeceb;
  color: #c0524b;
}

.status-open {
  background: #edf7f0;
  color: #184e37;
}

.status-closed {
  background: #f0f0f0;
  color: #888;
}

.trek-name {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
  color: #222;
  margin-bottom: 4px;
}

.trek-location {
  color: #8a8a8a;
  font-size: 0.9rem;
  margin-bottom: 16px;
}

.trek-meta {
  display: flex;
  gap: 18px;
  margin-bottom: 12px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: #3b3b3b;
}

.meta-item i {
  color: #184e37;
}

.trek-dates {
  font-size: 0.82rem;
  color: #8a8a8a;
  margin-bottom: 18px;
}

.trek-footer {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid #f0f0f0;
}

.staff-tag {
  font-size: 0.78rem;
  color: #8a8a8a;
}

.btn-book {
  background: #184e37;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 8px 18px;
  font-weight: 600;
  font-size: 0.85rem;
  transition: background 0.2s ease;
}

.btn-book:hover:not(:disabled) {
  background: #133d2b;
}

.btn-book:disabled {
  background: #d8d8d8;
  color: #999;
  cursor: not-allowed;
}
</style>

