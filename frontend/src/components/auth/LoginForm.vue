<template>
  <div class="card shadow border-0 p-5 auth-card">
    <h2 class="fw-bold">Welcome Back</h2>

    <p class="text-muted mb-4">Sign in to continue</p>

    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="login-email">Email</label>
        <input id="login-email" v-model="email" type="email" class="form-control" required />
      </div>

      <div class="mb-4">
        <label for="login-password">Password</label>

        <input
          id="login-password"
          v-model="password"
          type="password"
          class="form-control"
          required
        />
      </div>

      <button class="btn btn-primary-custom w-100">Login</button>

      <RouterLink class="d-block text-center mt-4" to="/register">
        Don't have an account?
      </RouterLink>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { loginUser } from '@/services/authService'
import { useAuthStore } from '@/store/auth'
import { useToastStore } from '@/store/toast'

const toast = useToastStore()
const router = useRouter()

const auth = useAuthStore()

const email = ref('')

const password = ref('')

async function login() {
  try {
    const response = await loginUser({
      email: email.value,

      password: password.value,
    })

    auth.setUser(response.data)

    if (response.data.role === 'admin') {
      router.push('/admin')
    } else if (response.data.role === 'staff') {
      router.push('/staff')
    } else {
      router.push('/')
    }
    toast.success('Login Successful')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Login Failed')
  }
}
</script>

<style scoped>
.auth-card {
  width: 430px;

  border-radius: 20px;
}
</style>
