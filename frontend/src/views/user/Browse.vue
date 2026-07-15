<template>
  <div class="browse-page">
    <div class="container py-5">
      <div class="page-header d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2 class="page-heading mb-1">Browse Treks</h2>
          <p class="page-subtext mb-0">Find your next adventure</p>
        </div>

        <div class="d-flex gap-3 align-items-center flex-wrap">
          <div class="search-wrap">
            <div class="input-group">
              <span class="input-group-text">
                <i class="bi bi-search"></i>
              </span>

              <input
                v-model="query"
                class="form-control"
                placeholder="Search Treks..."
                @input="search"
              />
            </div>
          </div>

          <select class="form-select filter-select" v-model="difficulty" @change="applyFilters">
            <option value="">All Difficulty</option>

            <option>Easy</option>

            <option>Moderate</option>

            <option>Hard</option>
          </select>

          <select class="form-select filter-select" v-model="location" @change="applyFilters">
            <option value="">All Locations</option>

            <option v-for="place in locations.filter(Boolean)" :key="place" :value="place">
              {{ place }}
            </option>
          </select>

          <select class="form-select filter-select" v-model="duration" @change="applyFilters">
            <option value="">Any Duration</option>

            <option :value="1">1 Day</option>

            <option :value="2">2 Days</option>

            <option :value="3">3 Days</option>

            <option :value="5">Up to 5 Days</option>

            <option :value="10">Up to 10 Days</option>
          </select>
        </div>
      </div>

      <Loader v-if="loading" />

      <EmptyState
        v-else-if="treks.length === 0"
        :title="searching ? 'No Matching Treks' : 'No Treks Available'"
        :message="
          searching
            ? 'Try different search or filter options.'
            : 'There are currently no treks available.'
        "
        :icon="searching ? 'bi bi-search' : 'bi bi-tree-fill'"
      />

      <div v-else class="row">
        <div class="col-md-4 mb-4" v-for="trek in treks" :key="trek.id">
          <TrekCard :trek="trek" @book="book" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

import Loader from '@/components/common/Loader.vue'
import TrekCard from '@/components/trek/TrekCard.vue'
import EmptyState from '@/components/common/EmptyState.vue'
import { getTreks, bookTrek } from '@/services/userService'
import { useAuthStore } from '@/store/auth'
import { useRouter } from 'vue-router'
import { useToastStore } from '@/store/toast'

const auth = useAuthStore()
const router = useRouter()
const toast = useToastStore()

const treks = ref([])
const loading = ref(false)
const query = ref('')

const allTreks = ref([])
const searching = ref(false)
const difficulty = ref('')
const location = ref('')
const duration = ref('')

const locations = computed(() => {
  return [...new Set(allTreks.value.map((trek) => trek.location))]
})

async function loadTreks() {
  loading.value = true

  try {
    const res = await getTreks()
    allTreks.value = res.data.treks
    applyFilters()
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load treks')
  } finally {
    loading.value = false
  }
}

function search() {
  searching.value = query.value.trim() !== ''
  applyFilters()
}

function applyFilters() {
  let filtered = [...allTreks.value]

  const q = query.value.toLowerCase().trim()

  if (q) {
    filtered = filtered.filter(
      (trek) =>
        (trek.trek_name || '').toLowerCase().includes(q) ||
        (trek.location || '').toLowerCase().includes(q) ||
        (trek.difficulty || '').toLowerCase().includes(q),
    )
  }

  if (difficulty.value) {
    filtered = filtered.filter((trek) => trek.difficulty === difficulty.value)
  }

  if (location.value) {
    filtered = filtered.filter((trek) => trek.location === location.value)
  }

  if (duration.value) {
    filtered = filtered.filter((trek) => Number(trek.duration) <= Number(duration.value))
  }

  treks.value = filtered
}

async function book(id) {
  if (!auth.loggedIn) {
    router.push({
      name: 'login',
      query: {
        redirect: '/browse',
      },
    })
    return
  }

  try {
    await bookTrek(id)

    toast.success('Trek Booked Successfully')

    query.value = ''
    difficulty.value = ''
    location.value = ''
    duration.value = ''
    searching.value = false

    await loadTreks()
  } catch (err) {
    toast.error(err.response?.data?.message || 'Booking Failed')
  }
}

onMounted(loadTreks)
</script>

<style scoped>
.browse-page {
  background: #faf8f3;
  min-height: 100vh;
}

.page-heading {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
  color: #222;
}

.page-subtext {
  color: #8a8a8a;
  font-size: 0.95rem;
}

.search-wrap {
  width: 320px;
}

.search-wrap .input-group-text {
  background: #fff;
  border: 1px solid #dcdcdc;
  border-right: none;
  color: #8a8a8a;
  border-radius: 10px 0 0 10px;
}

.search-wrap .form-control {
  border: 1px solid #dcdcdc;
  border-left: none;
  border-radius: 0 10px 10px 0;
  padding: 10px 14px;
}

.search-wrap .form-control:focus {
  border-color: #184e37;
  box-shadow: none;
}

.empty-wrap i {
  color: #a9cdba;
}

.empty-wrap h3 {
  color: #222;
}

.filter-select {
  width: 170px;

  border-radius: 10px;
}

.filter-select:focus {
  border-color: #184e37;

  box-shadow: 0 0 0 0.2rem rgba(24, 78, 55, 0.15);
}
</style>
