<template>
  <div class="card shadow border-0 p-5 auth-card">
    <h2 class="fw-bold">Welcome Back</h2>

    <p class="text-muted mb-4">Sign in to continue</p>

    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="login-email" class="form-label">Email</label>
        <input id="login-email" v-model="email" type="email" class="form-control" required />
      </div>

      <div class="mb-4">
        <label for="login-password" class="form-label">Password</label>

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

    auth.setUser({
      id: response.data.user_id,
      name: response.data.name,
      role: response.data.role
    })

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