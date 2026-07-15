<template>
  <div v-if="show" class="modal fade show d-block" style="background: rgba(0, 0, 0, 0.45)">
    <div class="modal-dialog modal-lg">
      <div class="modal-content staff-modal">
        <form @submit.prevent="saveStaff">
          <div class="modal-header">
            <h5 class="modal-title">
              {{ form.id ? 'Edit Staff' : 'Add Staff' }}
            </h5>

            <button class="btn-close" @click="$emit('close')"></button>
          </div>

          <div class="modal-body">
            <div class="row">
              <div class="col-md-6 mb-3">
                <label class="form-label">Full Name</label>

                <input v-model="form.full_name" class="form-control" required />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label">Email</label>

                <input type="email" v-model="form.email" class="form-control" required />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label">Contact Number</label>

                <input v-model="form.contact_number" class="form-control" required />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label">Experience (Years)</label>

                <input
                  type="number"
                  min="0"
                  v-model.number="form.experience"
                  class="form-control"
                />
              </div>

              <div class="col-md-12 mb-3">
                <label class="form-label">Specialization</label>

                <input v-model="form.specialization" class="form-control" />
              </div>

              <div v-if="!form.id" class="col-md-12">
                <label class="form-label">Password</label>

                <input type="password" v-model="form.password" class="form-control" required />
              </div>
            </div>
          </div>

          <div class="modal-footer">
            <button class="btn btn-cancel" type="button" @click="$emit('close')">Cancel</button>

            <button class="btn btn-save">
              {{ form.id ? 'Update Staff' : 'Create Staff' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue'

import { createStaff, updateStaff } from '@/services/adminService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const emit = defineEmits(['saved', 'close'])

const props = defineProps({
  selectedStaff: Object,
  show: Boolean,
})

const emptyForm = () => ({
  id: null,
  full_name: '',
  email: '',
  password: '',
  contact_number: '',
  specialization: '',
  experience: 0,
})

const form = reactive(emptyForm())

watch(
  () => props.selectedStaff,
  (value) => {
    Object.assign(form, emptyForm())

    if (value) {
      Object.assign(form, value)

      form.password = ''
    }
  },
  {
    immediate: true,
  },
)

async function saveStaff() {
  try {
    if (form.id) {
      await updateStaff(form.id, form)
      toast.success('Staff Updated')
    } else {
      await createStaff(form)
      toast.success('Staff Created')
    }

    emit('saved')
    emit('close')
    
  } catch (err) {
    console.error(err)

    toast.error(err.response?.data?.message || err.message || 'Operation Failed')
  }
}
</script>

<style scoped>
.staff-modal {
  border: none;
  border-radius: 18px;
  overflow: hidden;
}

.modal-header {
  background: #184e37;
  border-bottom: none;
  padding: 20px 28px;
}

.modal-title {
  color: #fff;
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
}

.modal-header .btn-close {
  filter: invert(1) brightness(2);
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

.form-control {
  border-radius: 10px;
  border: 1px solid #dcdcdc;
  padding: 9px 12px;
}

.form-control:focus {
  border-color: #184e37;
  box-shadow: 0 0 0 3px rgba(24, 78, 55, 0.15);
}

.modal-footer {
  padding: 18px 28px;
  border-top: 1px solid #ececec;
}

.btn-cancel {
  border: 1px solid #dcdcdc;
  border-radius: 10px;
  background: #fff;
  padding: 9px 20px;
  font-weight: 600;
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
