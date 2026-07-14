<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between mb-4">
      <h2>Treks</h2>

      <button
        class="btn btn-success"
        @click="selectedTrek = null"
        data-bs-toggle="modal"
        data-bs-target="#trekModal"
      >
        + Add Trek
      </button>
    </div>

    <SearchBar @search="handleSearch" />
    <Loader v-if="loading" />

    <EmptyState v-else-if="treks.length === 0" />

    <DataTable v-else :treks="treks" @edit="editTrek" @delete="deleteTrek" />
    <TrekModal :selectedTrek="selectedTrek" @saved="loadTreks" />
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'

import SearchBar from '@/components/dashboard/SearchBar.vue'

import DataTable from '@/components/dashboard/DataTable.vue'

import TrekModal from '@/components/dashboard/TrekModal.vue'

import { getTreks, searchTreks, removeTrek } from '@/services/adminService'
import Loader from '@/components/common/Loader.vue'
import EmptyState from '@/components/common/EmptyState.vue'
import { useToastStore } from '@/store/toast'

const toast = useToastStore()
const treks = ref([])

const search = ref('')

const selectedTrek = ref(null)
const loading = ref(false)

async function loadTreks() {
  loading.value = true

  try {
    const response = await getTreks()

    treks.value = response.data
  }catch (err) {
    toast.error(err.response?.data?.message || 'Failed to load treks')
  }
  finally {
    loading.value = false
  }
}

function editTrek(trek) {
  selectedTrek.value = trek
}

async function deleteTrek(trek) {
  if (!confirm(`Delete ${trek.trek_name}?`)) {
    return
  }

  await removeTrek(trek.id)
  toast.success('Trek Closed Successfully')
  loadTreks()
}

async function handleSearch(query) {
  if (query.trim() === '') {
    loadTreks()
    return
  }

  try {
    const response = await searchTreks(query)
    treks.value = response.data
  } catch (err) {
    console.log(err)
  }
}

onMounted(loadTreks)
</script>
