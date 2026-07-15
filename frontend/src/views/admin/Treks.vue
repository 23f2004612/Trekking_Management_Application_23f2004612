<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-heading mb-1">Treks</h2>
        <p class="page-subtext mb-0">Manage all trekking packages</p>
      </div>

      <button class="btn-add-trek" @click="addTrek">
        <i class="bi bi-plus-lg me-1"></i>
        Add Trek
      </button>
    </div>

    <SearchBar @search="handleSearch" />
    <Loader v-if="loading" />

    <EmptyState v-else-if="treks.length === 0" />

    <DataTable v-else :treks="treks" @edit="editTrek" @delete="deleteTrek" />
    <TrekModal
      :selectedTrek="selectedTrek"
      :show="showTrekModal"
      @close="showTrekModal = false"
      @saved="loadTreks"
    />
  </DashboardLayout>
</template>

<style scoped>
.page-heading {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
  color: #222;
}

.page-subtext {
  color: #8a8a8a;
  font-size: 0.9rem;
}

.btn-add {
  background: #184e37;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  transition: background 0.2s ease;
}

.btn-add:hover {
  background: #133d2b;
  color: #fff;
}

.btn-add-trek {
  background: #184e37;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  transition: background 0.2s ease;
}
</style>

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
const showTrekModal = ref(false)

const loading = ref(false)

async function loadTreks() {
  loading.value = true

  try {
    const response = await getTreks()

    treks.value = response.data
  } catch (err) {
    toast.error(err.response?.data?.message || 'Failed to load treks')
  } finally {
    loading.value = false
  }
}

function addTrek() {
  selectedTrek.value = null
  showTrekModal.value = true
}

function editTrek(trek) {
  selectedTrek.value = { ...trek }
  showTrekModal.value = true
}

async function deleteTrek(trek) {
  if (!confirm(`Close Trek - ${trek.trek_name}?`)) {
    return
  }

  try {
    await removeTrek(trek.id)

    toast.success('Trek Closed Successfully')

    loadTreks()
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
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
    toast.error(err.response?.data?.message || 'Search Failed')
  }
}

onMounted(loadTreks)
</script>
