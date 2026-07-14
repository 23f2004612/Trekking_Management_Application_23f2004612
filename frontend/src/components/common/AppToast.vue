<template>
  <div class="toast-container position-fixed top-0 end-0 p-3">
    <div
      class="toast fade show"
      :class="`text-bg-${toast.type}`"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      v-if="toast.show"
    >
      <div class="d-flex">
        <div class="toast-body">
          {{ toast.message }}
        </div>

        <button class="btn-close btn-close-white me-2 m-auto" @click="toast.show = false"></button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useToastStore } from '@/store/toast'

const toast = useToastStore()
</script>
