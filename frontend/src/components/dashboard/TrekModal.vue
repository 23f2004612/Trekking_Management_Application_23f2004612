<template>
  <div v-if="show" class="modal fade show d-block" style="background: rgba(0, 0, 0, 0.45)">
    <div class="modal-dialog modal-lg">
      <div class="modal-content trek-modal">
        <form @submit.prevent="saveTrek">
          <!-- Header -->

          <div class="modal-header">
            <h5 class="modal-title">
              {{ form.id ? 'Edit Trek' : 'Add Trek' }}
            </h5>

            <button type="button" class="btn-close" @click="$emit('close')"></button>
          </div>

          <!-- Body -->

          <div class="modal-body">
            <div class="row">
              <!-- Trek Name -->
              <div class="col-md-6 mb-3">
                <label class="form-label">Trek Name</label>
                <input v-model="form.trek_name" class="form-control" required />
              </div>

              <!-- Location -->
              <div class="col-md-6 mb-3">
                <label class="form-label">Location</label>
                <input v-model="form.location" class="form-control" required />
              </div>

              <!-- Difficulty -->
              <div class="col-md-4 mb-3">
                <label class="form-label">Difficulty</label>

                <select v-model="form.difficulty" class="form-select">
                  <option>Easy</option>
                  <option>Moderate</option>
                  <option>Hard</option>
                </select>
              </div>

              <!-- Status -->
              <div class="col-md-4 mb-3">
                <label class="form-label">Status</label>

                <select v-model="form.status" class="form-select">
                  <option>Open</option>
                  <option>Closed</option>
                </select>
              </div>

              <!-- Duration -->
              <div class="col-md-4 mb-3">
                <label class="form-label">Duration (Days)</label>

                <input type="number" min="1" v-model.number="form.duration" class="form-control" />
              </div>

              <!-- Available Slots -->
              <div class="col-md-4 mb-3">
                <label class="form-label">Available Slots</label>

                <input
                  type="number"
                  min="1"
                  v-model.number="form.available_slots"
                  class="form-control"
                />
              </div>

              <!-- Booked Slots -->
              <div class="col-md-4 mb-3">
                <label class="form-label">Booked Slots</label>

                <input class="form-control" :value="form.booked_slots" readonly />
              </div>

              <!-- Assign Staff -->
              <div class="col-md-4 mb-3">
                <label class="form-label">Assign Staff</label>

                <select v-model.number="form.assigned_staff_id" class="form-select">
                  <option :value="null">Select Staff</option>

                  <option v-for="staff in staffList" :key="staff.id" :value="staff.id">
                    {{ staff.full_name }}
                  </option>
                </select>
              </div>

              <!-- Start Date -->
              <div class="col-md-6 mb-3">
                <label class="form-label">Start Date</label>

                <input type="date" v-model="form.start_date" class="form-control" />
              </div>

              <!-- End Date -->
              <div class="col-md-6 mb-3">
                <label class="form-label">End Date</label>

                <input type="date" v-model="form.end_date" class="form-control" />
              </div>

              <!-- Description -->
              <div class="col-12">
                <label class="form-label">Description</label>

                <textarea rows="4" v-model="form.description" class="form-control"></textarea>
              </div>
            </div>
          </div>

          <!-- Footer -->

          <div class="modal-footer">
            <button type="button" class="btn btn-cancel" @click="$emit('close')">Cancel</button>

            <button class="btn btn-save">
              {{ form.id ? 'Update Trek' : 'Create Trek' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, watch, onMounted } from 'vue'

import { createTrek, updateTrek, getStaff } from '@/services/adminService'
import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const emit = defineEmits(['saved', 'close'])

const props = defineProps({
  selectedTrek: Object,
  show: Boolean,
})

const emptyForm = () => ({
  id: null,
  trek_name: '',
  location: '',
  description: '',
  difficulty: 'Easy',
  duration: 1,
  available_slots: 1,
  booked_slots: 0,
  assigned_staff_id: null,
  status: 'Open',
  start_date: '',
  end_date: '',
})

const form = reactive(emptyForm())

const staffList = ref([])

watch(
  () => props.selectedTrek,
  (value) => {
    Object.assign(form, emptyForm())

    if (value) {
      form.id = value.id
      form.trek_name = value.trek_name
      form.location = value.location
      form.description = value.description
      form.difficulty = value.difficulty
      form.duration = value.duration
      form.available_slots = value.available_slots
      form.booked_slots = value.booked_slots
      form.status = value.status
      form.start_date = value.start_date
      form.end_date = value.end_date

      form.assigned_staff_id = value.staff?.id ?? value.assigned_staff_id ?? null
    }
  },
  {
    immediate: true,
  },
)

console.log("Selected:", form.assigned_staff_id)
console.log("Staff List:", staffList.value)

async function loadStaff() {
  try {
    const response = await getStaff()

    staffList.value = response.data
  } catch (err) {
    console.error(err)
  }
}

async function saveTrek() {
  const payload = {
    trek_name: form.trek_name,
    location: form.location,
    description: form.description,
    difficulty: form.difficulty,
    duration: form.duration,
    available_slots: form.available_slots,
    assigned_staff_id: form.assigned_staff_id,
    status: form.status,
    start_date: form.start_date,
    end_date: form.end_date,
  }

  try {
    if (form.id) {
      await updateTrek(form.id, payload)
      toast.success('Trek Updated')
    } else {
      await createTrek(payload)
      toast.success('Trek Created')
    }

    Object.assign(form, emptyForm())

    emit('saved')
    emit('close')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
}

onMounted(loadStaff)
</script>

<style scoped>
.trek-modal {
  border: none;
  border-radius: 18px;
  overflow: hidden;
}

.modal-header {
  background: #184e37;
  padding: 20px 28px;
  border-bottom: none;
}

.modal-title {
  color: #fff;
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
}

.modal-header .btn-close {
  filter: invert(1) brightness(2);
  opacity: 0.85;
}

.modal-body {
  padding: 28px;
}

.form-label {
  font-weight: 600;
  font-size: 0.85rem;
  color: #3b3b3b;
  margin-bottom: 6px;
}

.form-control,
.form-select {
  border: 1px solid #dcdcdc;
  border-radius: 10px;
  padding: 9px 12px;
}

.form-control:focus,
.form-select:focus {
  border-color: #184e37;
  box-shadow: 0 0 0 3px rgba(24, 78, 55, 0.15);
}

.modal-footer {
  border-top: 1px solid #ececec;
  padding: 18px 28px;
}

.btn-cancel {
  background: #fff;
  border: 1px solid #dcdcdc;
  color: #555;
  border-radius: 10px;
  padding: 9px 20px;
  font-weight: 600;
}

.btn-cancel:hover {
  background: #f5f5f5;
  color: #333;
}

.btn-save {
  background: #184e37;
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: 9px 22px;
  font-weight: 600;
}

.btn-save:hover {
  background: #133d2b;
  color: #fff;
}
</style>
