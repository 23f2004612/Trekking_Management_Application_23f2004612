
<template>
  <DashboardLayout>
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h2 class="page-title">Staff Management</h2>
        <p class="text-muted mb-0">Create, update and manage trekking staff.</p>
      </div>

      <button class="btn-add-staff" @click="addStaff">
        <i class="bi bi-plus-lg me-1"></i>
            Add Staff
      </button>
    </div>

    <SearchBar @search="searchStaffData" />

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="staff.length === 0"
      title="No Staff Found"
      message="Add your first staff member."
    />

    <div v-else class="table-card mt-4">
      <div class="table-responsive">
        <table class="table align-middle mb-0">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Contact</th>
              <th>Specialization</th>
              <th>Experience</th>
              <th>Status</th>
              <th class="text-center">Actions</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="member in staff" :key="member.id">
              <td class="fw-semibold">
                {{ member.full_name }}
              </td>

              <td class="text-muted-cell">
                {{ member.email }}
              </td>

              <td>
                {{ member.contact_number }}
              </td>

              <td>
                <span v-if="member.specialization" class="badge badge-spec">
                  {{ member.specialization }}
                </span>

                <span v-else class="text-muted-cell">—</span>
              </td>

              <td>{{ member.experience }} yrs</td>

              <td>
                <span
                  class="badge"
                  :class="member.status === 'active' ? 'badge-active' : 'badge-blacklisted'"
                >
                  {{ member.status }}
                </span>
              </td>

              <td class="text-center">
                <!-- Edit -->
                <button
                  class="action-icon-btn edit-btn me-2"
                  :disabled="member.status === 'blacklisted'"
                  @click="editStaff(member)"
                  title="Edit Staff"
                >
                  <i class="bi bi-pencil"></i>
                </button>

                <!-- Active Staff -->
                <template v-if="member.status === 'active'">
                  <button class="action-btn blacklist-btn me-2" @click="deleteStaff(member.id)">
                    <i class="bi bi-slash-circle me-1"></i>
                    Blacklist
                  </button>
                </template>

                <!-- Blacklisted Staff -->
                <template v-else>
                  <button class="action-btn activate-btn" @click="toggleStatus(member, 'active')">
                    <i class="bi bi-check-circle me-1"></i>
                    Activate
                  </button>
                </template>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <StaffModal
      :selectedStaff="selectedStaff"
      :show="showStaffModal"
      @close="showStaffModal = false"
      @saved="loadStaff"
    />
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import DashboardLayout from '@/components/dashboard/DashboardLayout.vue'
import SearchBar from '@/components/dashboard/SearchBar.vue'
import Loader from '@/components/common/Loader.vue'
import EmptyState from '@/components/common/EmptyState.vue'
import StaffModal from '@/components/dashboard/StaffModal.vue'

import { getStaff, removeStaff, searchStaff, updateStaff } from '@/services/adminService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const staff = ref([])

const loading = ref(false)

const selectedStaff = ref(null)
const showStaffModal = ref(false)

async function loadStaff() {
  loading.value = true

  try {
    const res = await getStaff()

    staff.value = res.data
  } catch (err) {
    toast.error(err.response?.data?.message || 'Unable to load staff.')
  } finally {
    loading.value = false
  }
}

function addStaff() {
  selectedStaff.value = null
  showStaffModal.value = true
}

function editStaff(member) {
  selectedStaff.value = { ...member }
  showStaffModal.value = true
}

async function deleteStaff(id) {
  if (!confirm('Deactivate this staff member?')) return

  try {
    await removeStaff(id)

    toast.success('Staff Deactivated')

    loadStaff()
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
}

async function searchStaffData(query) {
  if (!query.trim()) {
    loadStaff()
    return
  }

  try {
    const res = await searchStaff(query)

    staff.value = res.data
  } catch (err) {
    toast.error(err.response?.data?.message || 'Search Failed')
  }
}

async function toggleStatus(member, status) {
  try {
    await updateStaff(member.id, {
      status: status,
    })

    member.status = status

    toast.success(status === 'active' ? 'Staff Activated' : 'Staff Blacklisted')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
}

onMounted(loadStaff)
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

.badge-spec {
  background: #edf7f0;
  color: #184e37;
  text-transform: none;
}

.badge-active {
  background: #edf7f0;
  color: #184e37;
}

.badge-blacklisted {
  background: #fbeceb;
  color: #c0524b;
}

.action-icon-btn {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  border: 1px solid #e2e2e2;
  background: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition:
    background 0.2s ease,
    color 0.2s ease,
    border-color 0.2s ease;
}

.edit-btn {
  color: #184e37;
}

.edit-btn:hover {
  background: #edf7f0;
  border-color: #184e37;
}

.delete-btn {
  color: #c0524b;
}

.delete-btn:hover {
  background: #fbeceb;
  border-color: #c0524b;
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
  transition:
    background 0.2s ease,
    color 0.2s ease;
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

.action-icon-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.action-icon-btn:disabled:hover {
  background: #fff;
  border-color: #e2e2e2;
}

.btn-add-staff {
  background: #184e37;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  transition: background 0.2s ease;
}

</style>
