<template>
  <div class="card shadow border-0 p-5 auth-card">
    <h2 class="fw-bold">Create Account</h2>

    <p class="text-muted">Join Trailhead today.</p>

    <form @submit.prevent="register">
      <div class="mb-3">
        <label class="form-label">Full Name</label>

        <input v-model="form.full_name" class="form-control" required />
      </div>

      <div class="mb-3">
        <label class="form-label">Email</label>
        <input v-model="form.email" type="email" class="form-control" required />
      </div>

      <div class="mb-3">
        <label class="form-label">Phone</label>

        <input v-model="form.contact_number" class="form-control" />
      </div>

      <div class="mb-4">
        <label class="form-label">Password</label>
        <input v-model="form.password" type="password" class="form-control" required />
      </div>

      <button class="btn btn-primary-custom w-100">Create Account</button>

      <RouterLink class="d-block text-center mt-4" to="/login">
        Already have an account?
      </RouterLink>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'

import { registerUser } from '@/services/authService'
import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const router = useRouter()

const form = reactive({
  full_name: '',
  email: '',
  contact_number: '',
  password: '',
})

async function register() {
  try {
    await registerUser(form)

    toast.success('Registration Successful')

    router.push('/login')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Registration Failed')
  }
}
</script>

<style scoped>
.auth-card {
  width: 450px;
  border-radius: 20px;
}

.form-label {
  font-weight: 600;
  font-size: 0.9rem;
  color: #3b3b3b;
  margin-bottom: 6px;
}

.form-control {
  padding: 10px 14px;
  border-radius: 10px;
  border: 1px solid #dcdcdc;
}

.form-control:focus {
  border-color: #184e37;
  box-shadow: 0 0 0 3px rgba(24, 78, 55, 0.15);
}

.btn-primary-custom {
  background: #184e37;
  color: #fff;
  border-radius: 10px;
  padding: 10px;
  font-weight: 600;
  width: 100%;
  transition: background 0.2s ease;
}

.btn-primary-custom:hover {
  background: #133d2b;
  color: #fff;
}
</style>