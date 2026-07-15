<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-heading mb-1">Assigned Treks</h2>
        <p class="page-subtext mb-0">Manage your assigned treks and participants.</p>
      </div>
    </div>

    <SearchBar @search="filterTreks" />

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="treks.length === 0"
      :title="searching ? 'No Matching Treks' : 'No Assigned Treks'"
      :message="
        searching
          ? 'Try searching with a different keyword.'
          : 'No treks have been assigned to you yet.'
      "
      :icon="searching ? 'bi bi-search' : 'bi bi-signpost'"
    />

    <StaffTreksTable v-else :treks="treks" @manage="editTrek" @complete="complete" />

    <ManageTrekModal
      :show="showModal"
      :selectedTrek="selectedTrek"
      @saved="loadTreks"
      @close="showModal = false"
    />
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import SearchBar from '@/components/dashboard/SearchBar.vue'

import Loader from '@/components/common/Loader.vue'
import EmptyState from '@/components/common/EmptyState.vue'

import StaffTreksTable from '@/components/staff/StaffTreksTable.vue'
import ManageTrekModal from '@/components/staff/ManageTrekModal.vue'

import { getAssignedTreks, completeTrek } from '@/services/staffService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const loading = ref(false)

const treks = ref([])

const allTreks = ref([])

const showModal = ref(false)

const selectedTrek = ref(null)
const searching = ref(false)

async function loadTreks() {
  loading.value = true

  try {
    const res = await getAssignedTreks()

    treks.value = res.data

    allTreks.value = [...res.data]
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load treks')
  } finally {
    loading.value = false
  }
}

function editTrek(trek) {
  selectedTrek.value = {
    ...trek,
  }

  showModal.value = true
}

async function complete(trek) {
  if (!confirm('Mark trek as completed?')) {
    return
  }

  try {
    await completeTrek(trek.id)

    toast.success('Trek Completed')

    loadTreks()
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
}

function filterTreks(value = '') {
  const q = value.toLowerCase().trim()

  searching.value = value.trim() !== "";

  if (!q) {
    treks.value = [...allTreks.value]
    return
  }

  treks.value = allTreks.value.filter(
    (trek) =>
      trek.trek_name.toLowerCase().includes(q) ||
      (trek.location || '').toLowerCase().includes(q) ||
      trek.status.toLowerCase().includes(q) ||
      trek.difficulty.toLowerCase().includes(q),
  )
}

onMounted(loadTreks)
</script>
