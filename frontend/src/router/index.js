import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import { useAuthStore } from '@/store/auth'
import AdminDashboard from '@/views/admin/Dashboard.vue'
import Treks from '@/views/admin/Treks.vue'
import Browse from '@/views/user/Browse.vue'
import Bookings from '@/views/user/Bookings.vue'
import Staff from '@/views/admin/Staff.vue'

import StaffTrekBookings from '@/views/staff/TrekBookings.vue'
import StaffDashboard from '@/views/staff/Dashboard.vue'
import StaffTreks from "@/views/staff/StaffTreks.vue";

import Users from '@/views/admin/Users.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },

  {
    path: '/login',
    name: 'login',
    component: Login,
  },

  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/browse',
    component: Browse,
  },
  {
    path: '/bookings',
    component: Bookings,
    meta: {
      requiresAuth: true,
      requiredRole: 'user',
    },
  },
  {
    path: '/admin',
    component: AdminDashboard,
    meta: { requiresAuth: true, requiredRole: 'admin' },
  },
  {
    path: '/admin/treks',
    component: Treks,
    meta: { requiresAuth: true, requiredRole: 'admin' },
  },
  {
    path: '/admin/staff',
    component: Staff,
    meta: {
      requiresAuth: true,
      role: 'admin',
    },
  },
  {
    path: '/admin/users',
    component: Users,
    meta: {
      requiresAuth: true,
      role: 'admin',
    },
  },
  {
    path: '/staff',
    component: StaffDashboard,
    meta: {
      requiresAuth: true,
      requiredRole: 'staff',
    },
  },
  {
    path: '/staff/treks',
    component: StaffTreks,
    meta: {
      requiresAuth: true,
      requiredRole: 'staff',
    },
  },
  {
    path: '/staff/trek/:id',
    component: StaffTrekBookings,
    meta: {
      requiresAuth: true,
      requiredRole: 'staff',
    },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()

  // Prevent logged-in users from visiting Login/Register
  if (auth.loggedIn && (to.path === '/login' || to.path === '/register')) {
    if (auth.role === 'admin') {
      return next('/admin')
    }

    if (auth.role === 'staff') {
      return next('/staff')
    }

    return next('/')
  }

  if (to.meta.requiresAuth) {
    if (!auth.loggedIn) {
      return next('/login')
    }

    if (to.meta.requiredRole && auth.role !== to.meta.requiredRole) {
      return next('/')
    }
  }

  next()
})

export default router
