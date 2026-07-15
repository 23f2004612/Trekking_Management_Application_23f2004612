<template>
  <div class="browse-page">
    <div class="container py-5">
      <div class="page-header d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2 class="page-heading mb-1">Browse Treks</h2>
          <p class="page-subtext mb-0">Find your next adventure</p>
        </div>

        <div class="search-wrap">
          <div class="input-group">
            <span class="input-group-text">
              <i class="bi bi-search"></i>
            </span>
            <input
              v-model="query"
              class="form-control"
              placeholder="Search treks..."
              @input="search"
            />
          </div>
        </div>
      </div>

      <Loader v-if="loading" />

      <div v-else-if="treks.length === 0" class="empty-wrap text-center py-5">
        <i class="bi bi-tree-fill display-1"></i>
        <h3 class="mt-4 fw-bold">No Treks Available</h3>
        <p class="text-muted mb-0">
          There are currently no treks available. Please check back later.
        </p>
      </div>

      <div v-else class="row">
        <div class="col-md-4 mb-4" v-for="trek in treks" :key="trek.id">
          <TrekCard :trek="trek" @book="book" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import Loader from '@/components/common/Loader.vue'
import TrekCard from '@/components/trek/TrekCard.vue'

import { getTreks, searchTreks, bookTrek } from '@/services/userService'
import { useAuthStore } from "@/store/auth";
import { useRouter } from "vue-router";

const auth = useAuthStore();
const router = useRouter();

const treks = ref([])
const loading = ref(false)
const query = ref('')

async function loadTreks() {
  loading.value = true
  const res = await getTreks()
  treks.value = res.data.treks
  loading.value = false
}

async function search() {
  if (query.value === '') {
    loadTreks()
    return
  }

  const res = await searchTreks(query.value)
  treks.value = res.data
}

async function book(id) {

  if (!auth.user) {
    router.push({
      name: "login",
      query: {
        redirect: "/browse",
      },
    });
    return;
  }

  try {
    await bookTrek(id);
    loadTreks();
  } catch (err) {
    toast.error(
      err.response?.data?.message ||
      "Booking Failed"
    );
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
</style>