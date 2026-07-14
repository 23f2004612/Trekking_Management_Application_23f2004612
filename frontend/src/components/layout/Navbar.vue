<script setup>

import { useRouter } from "vue-router";

import { useAuthStore } from "@/store/auth";

import { logoutUser } from "@/services/authService";

const router = useRouter();

const auth = useAuthStore();

async function logout(){

    await logoutUser();

    auth.logout();

    router.push("/");

}

</script>

<template>
  <nav class="navbar navbar-expand-lg bg-white shadow-sm">
    <div class="container">
      <RouterLink to="/" class="navbar-brand d-flex align-items-center">
        <div class="logo me-3">
          <i class="bi bi-image-alt"></i>
        </div>

        <div>
          <h3 class="mb-0 fw-bold">Trailhead</h3>

          <small> TREKKING MGMT </small>
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
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/"> Home </RouterLink>
          </li>

          <li class="nav-item">
            <RouterLink class="nav-link" to="/browse"> Browse Treks </RouterLink>
          </li>

          <li class="nav-item">
            <RouterLink class="nav-link" to="/bookings"> My Bookings </RouterLink>
          </li>

          <li class = "nav-item">
            <RouterLink v-if="auth.loggedIn && auth.role === 'admin'" to="/admin" class="nav-link">
              Dashboard
            </RouterLink>

            <RouterLink
              v-else-if="auth.loggedIn && auth.role === 'staff'"
              to="/staff"
              class="nav-link"
            >
              Dashboard
            </RouterLink>

            <RouterLink v-else-if="auth.loggedIn" to="/user" class="nav-link"> Dashboard </RouterLink>
          </li>
        </ul>

        <div v-if="!auth.loggedIn">
          <RouterLink to="/login" class="btn btn-link"> Log in </RouterLink>

          <RouterLink to="/register" class="btn btn-primary-custom rounded-3 ms-3">
            Sign up
          </RouterLink>
        </div>

        <div v-else class="dropdown">
          <button class="btn btn-success dropdown-toggle" data-bs-toggle="dropdown">
            {{ auth.user.name }}
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
.logo {
  width: 44px;

  height: 44px;

  background: #184e37;

  border-radius: 10px;

  display: flex;

  justify-content: center;

  align-items: center;

  color: white;

  font-size: 1.3rem;
}

.nav-link {
  margin: 0 12px;

  font-weight: 600;

  color: #555;
}

.router-link-active {
  color: #184e37 !important;

  font-weight: 700;
}

small {
  letter-spacing: 2px;

  color: #777;
}
</style>
