<template>
  <div class="dashboard">
    <DashboardSidebar />

    <div class="main">
      <DashboardNavbar />

      <div class="content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup>
import DashboardSidebar from './DashboardSidebar.vue'
</script>

<style scoped>
.dashboard {
  display: flex;
  min-height: 100vh;
  background: #d2cab7;
}

.main {
  flex: 1;
  min-width: 0;
}

.content {
  padding: 30px;
}
</style>