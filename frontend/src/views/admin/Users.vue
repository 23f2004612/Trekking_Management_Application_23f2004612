<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-title">User Management</h2>
        <p class="text-muted mb-0">View and manage registered users.</p>
      </div>
    </div>

    <SearchBar @search="searchUserData" />

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="users.length === 0"
      title="No Users Found"
      message="No registered users available."
    />

    <div v-else class="table-card mt-4">
      <div class="table-responsive">
        <table class="table align-middle mb-0">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Contact</th>
              <th>Joined</th>
              <th>Status</th>
              <th class="text-center">Action</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td class="fw-semibold">
                {{ user.full_name }}
              </td>

              <td class="text-muted-cell">
                {{ user.email }}
              </td>

              <td>
                {{ user.contact_number }}
              </td>

              <td class="text-muted-cell">
                {{ formatDate(user.created_at) }}
              </td>

              <td>
                <span
                  class="badge"
                  :class="user.status === 'active' ? 'badge-active' : 'badge-blacklisted'"
                >
                  {{ user.status }}
                </span>
              </td>

              <td class="text-center">
                <button
                  v-if="user.status === 'active'"
                  class="action-btn blacklist-btn"
                  @click="changeStatus(user, 'blacklisted')"
                >
                  <i class="bi bi-slash-circle me-1"></i>
                  Blacklist
                </button>

                <button
                  v-else
                  class="action-btn activate-btn"
                  @click="changeStatus(user, 'active')"
                >
                  <i class="bi bi-check-circle me-1"></i>
                  Activate
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import SearchBar from '@/components/dashboard/SearchBar.vue'
import Loader from '@/components/common/Loader.vue'
import EmptyState from '@/components/common/EmptyState.vue'

import { getUsers, searchUsers, updateUserStatus } from '@/services/adminService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const users = ref([])
const loading = ref(false)

async function loadUsers() {
  loading.value = true

  try {
    const res = await getUsers()
    users.value = res.data
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load users.')
  } finally {
    loading.value = false
  }
}

async function searchUserData(query) {
  if (!query.trim()) {
    loadUsers()
    return
  }

  try {
    const res = await searchUsers(query)
    users.value = res.data
  } catch (err) {
    toast.error(err.response?.data?.message || 'Search Failed')
  }
}

async function changeStatus(user, status) {
  const message = status === 'blacklisted' ? 'Blacklist this user?' : 'Activate this user?'

  if (!confirm(message)) return

  try {
    await updateUserStatus(user.id, status)

    user.status = status

    toast.success(status === 'active' ? 'User Activated' : 'User Blacklisted')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
}

function formatDate(date) {
  if (!date) return '-'

  return new Date(date).toLocaleDateString('en-IN', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
  })
}

onMounted(loadUsers)
</script>

<style scoped>
.table-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.table-card .table > thead > tr > th {
  background: #faf8f3;
  color: #8a8a8a;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  padding: 16px 20px !important;
  border-bottom: 2px solid #ececec !important;
  vertical-align: middle;
}

.table-card .table > tbody > tr > td {
  padding: 16px 20px !important;
  color: #3b3b3b;
  border-bottom: 1px solid #f0f0f0 !important;
  border-top: none !important;
  font-size: 0.92rem;
  vertical-align: middle;
}

.table-card .table > tbody > tr:last-child > td {
  border-bottom: none !important;
}

.table-card .table > tbody > tr:hover > td {
  background-color: #faf8f3;
}

.text-muted-cell {
  color: #8a8a8a;
}

.badge {
  font-weight: 600;
  font-size: 0.72rem;
  padding: 6px 12px;
  border-radius: 999px;
  text-transform: capitalize;
}

.badge-active {
  background: #edf7f0;
  color: #184e37;
}

.badge-blacklisted {
  background: #fbeceb;
  color: #c0524b;
}

.action-btn {
  display: inline-flex;
  align-items: center;
  border: 1px solid;
  background: #fff;
  border-radius: 8px;
  padding: 6px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  transition: background 0.2s ease, color 0.2s ease;
}

.blacklist-btn {
  color: #c0524b;
  border-color: #e8b6b1;
}

.blacklist-btn:hover {
  background: #fbeceb;
}

.activate-btn {
  color: #184e37;
  border-color: #a9cdba;
}

.activate-btn:hover {
  background: #edf7f0;
}
.page-title {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
  color: #184e37;
}

.card {
  border-radius: 18px;
}

.table {
  margin: 0;
}

.table thead {
  background: #184e37;
  color: #fff;
}

.table thead th {
  border: none;
  padding: 16px;
  font-weight: 600;
  white-space: nowrap;
}

.table tbody td {
  padding: 16px;
  vertical-align: middle;
}

.table tbody tr {
  transition: 0.2s;
}

.table tbody tr:hover {
  background: #f7fbf8;
}

.badge {
  font-size: 0.75rem;
  padding: 7px 10px;
}

.btn-outline-danger,
.btn-outline-success {
  border-radius: 8px;
}

.text-muted {
  color: #6c757d !important;
}
</style>
