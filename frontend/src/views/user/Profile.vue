<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-title">My Profile</h2>
        <p class="text-muted mb-0">Update your personal information.</p>
      </div>
    </div>

    <Loader v-if="loading" />

    <div v-else class="profile-card">
      <form @submit.prevent="save">
        <div class="mb-4">
          <label class="form-label">Full Name</label>

          <input v-model="form.full_name" class="form-control" required />
        </div>

        <div class="mb-4">
          <label class="form-label">Email</label>

          <input type="email" v-model="form.email" class="form-control" required />
        </div>

        <div class="mb-4">
          <label class="form-label">Contact Number</label>

          <input v-model="form.contact_number" class="form-control" />
        </div>

        <button class="btn-save" :disabled="saving">
          <i class="bi bi-check-circle me-2"></i>
          Save Changes
        </button>
      </form>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import Loader from '@/components/common/Loader.vue'

import { getProfile, updateProfile } from '@/services/userService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const loading = ref(true)
const saving = ref(false)

const form = ref({
  full_name: '',
  email: '',
  contact_number: '',
})

async function loadProfile() {
  loading.value = true

  try {
    const res = await getProfile()

    form.value = { ...res.data }
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load profile.')
  } finally {
    loading.value = false
  }
}

async function save() {
  saving.value = true

  try {
    await updateProfile(form.value)

    toast.success('Profile updated successfully.')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to update profile.')
  } finally {
    saving.value = false
  }
}

onMounted(loadProfile)
</script>

<style scoped>
.page-title {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
}

.profile-card {
  background: white;

  border-radius: 18px;

  padding: 35px;

  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);

  max-width: 700px;
}

.form-label {
  font-weight: 600;

  color: #444;
}

.form-control {
  border-radius: 10px;

  padding: 11px 14px;
}

.form-control:focus {
  border-color: #184e37;

  box-shadow: 0 0 0 0.2rem rgba(24, 78, 55, 0.15);
}

.btn-save {
  background: #184e37;

  color: white;

  border: none;

  padding: 11px 28px;

  border-radius: 10px;

  font-weight: 600;
}

.btn-save:hover {
  background: #256046;
}

.btn-save:disabled {
  opacity: 0.6;

  cursor: not-allowed;
}
</style>
