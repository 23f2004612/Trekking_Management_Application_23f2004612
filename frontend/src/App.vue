<template>
  <Navbar />
  <AppToast />
  <RouterView />
</template>

<script setup>
import Navbar from './components/layout/Navbar.vue'
import AppToast from '@/components/common/AppToast.vue'
</script>
