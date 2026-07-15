<template>
  <div class="search-wrap mb-4">
    <div class="input-group">
      <span class="input-group-text">
        <i class="bi bi-search"></i>
      </span>

      <input v-model="search" class="form-control" placeholder="Search treks..." />
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const emit = defineEmits(['search'])

const search = ref('')

watch(search, (value) => {
  emit('search', value)
})
</script>

<style scoped>
.search-wrap {
  max-width: 380px;
}

.input-group-text {
  background: #fff;
  border: 1px solid #dcdcdc;
  border-right: none;
  color: #8a8a8a;
  border-radius: 10px 0 0 10px;
}

.form-control {
  border: 1px solid #dcdcdc;
  border-left: none;
  border-radius: 0 10px 10px 0;
  padding: 10px 14px;
}

.form-control:focus {
  border-color: #184e37;
  box-shadow: none;
}

.form-control:focus + .input-group-text,
.input-group:focus-within .input-group-text {
  border-color: #184e37;
}
</style>