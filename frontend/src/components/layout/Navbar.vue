<script setup>
import { useRouter, RouterLink } from 'vue-router'
import { useAuthStore } from '@/store/auth'
import { logoutUser } from '@/services/authService'

const router = useRouter()
const auth = useAuthStore()

async function logout() {
  await logoutUser()
  auth.logout()
  router.push('/')
}
</script>

<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container">
      <RouterLink to="/" class="navbar-brand d-flex align-items-center">
        <div class="d-flex align-items-center">
          <div class="logo me-3">
            <i class="bi bi-image-alt"></i>
          </div>

          <div>
            <h3>Trailhead</h3>
            <small>TREKKING MGMT</small>
          </div>
        </div>
      </RouterLink>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbar"
        aria-controls="navbar"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbar">
        <ul class="navbar-nav mx-auto align-items-center">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/"> Home </RouterLink>
          </li>

          <li v-if="!auth.loggedIn || auth.role === 'user'" class="nav-item">
            <RouterLink class="nav-link" to="/browse"> Browse Treks </RouterLink>
          </li>

          <li v-if="auth.loggedIn && auth.role === 'user'" class="nav-item">
            <RouterLink class="nav-link" to="/bookings">My Bookings</RouterLink>
          </li>
          <li v-if="auth.role === 'admin'" class="nav-item">
            <RouterLink class="nav-link" to="/admin">Dashboard</RouterLink>
          </li>
          <li v-else-if="auth.role === 'staff'" class="nav-item">
            <RouterLink class="nav-link" to="/staff">Dashboard</RouterLink>
          </li>
        </ul>

        <div v-if="!auth.loggedIn" class="d-flex align-items-center gap-2">
          <RouterLink to="/login" class="login-link">Log in</RouterLink>
          <RouterLink to="/register" class="btn btn-signup rounded-pill px-4 ms-2">
            Sign up
          </RouterLink>
        </div>

        <div v-else class="dropdown">
          <button
            class="btn btn-signup dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            {{ auth.user?.name || 'Account' }}
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li>
              <button class="dropdown-item" @click="logout">Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background: #faf8f3;
  max-height: 70px;
  padding: 14px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.logo {
  width: 40px;
  height: 40px;
  background: #184e37;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 1.15rem;
}

.navbar-nav {
  gap: 24px;
}

.nav-link {
  font-size: 1rem;
  font-weight: 600;
  color: #3b3b3b !important;
  padding: 6px 0 !important;
  transition: color 0.2s ease;
}

.nav-link:hover {
  color: #184e37 !important;
}

.nav-link.router-link-active {
  color: #184e37 !important;
  font-weight: 700;
}

.navbar-brand h3 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: #222;
  margin-bottom: 0;
}

.navbar-brand small {
  letter-spacing: 1.8px;
  font-size: 0.65rem;
  color: #8a8a8a;
}

.login-link {
  color: #222;
  font-weight: 600;
  text-decoration: none;
  padding: 9px 14px;
}

.login-link:hover {
  color: #184e37;
}

.btn-signup {
  background: #184e37;
  color: #fff !important;
  border: none;
  border-radius: 999px;
  padding: 9px 22px;
  font-weight: 600;
}

.btn-signup:hover,
.btn-signup:focus,
.btn-signup:active {
  color: #fff !important;
  background: #184e37 !important;
  border-color: #184e37 !important;
}

.btn-signup::after {
  color: #fff;
}

.dropdown-menu {
  border-radius: 14px;
  border: none;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
  overflow: hidden;
}

.dropdown-item {
  padding: 10px 18px;
  font-weight: 500;
}

.dropdown-item:hover {
  background: #edf7f0;
}

</style>
