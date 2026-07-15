<template>
  <div v-if="show" class="modal fade show d-block" style="background: rgba(0, 0, 0, 0.45)">
    <div class="modal-dialog modal-lg">
      <div class="modal-content trek-modal">
        <form @submit.prevent="save">
          <!-- Header -->

          <div class="modal-header">
            <h5 class="modal-title">Manage Trek</h5>

            <button class="btn-close" type="button" @click="$emit('close')"></button>
          </div>

          <!-- Body -->

          <div class="modal-body">
            <div class="row">
              <div class="col-md-6 mb-3">
                <label class="form-label"> Trek Name </label>

                <input class="form-control" :value="form.trek_name" readonly />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label"> Location </label>

                <input class="form-control" :value="form.location" readonly />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label"> Difficulty </label>

                <input class="form-control" :value="form.difficulty" readonly />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label"> Duration </label>

                <input class="form-control" :value="form.duration + ' Days'" readonly />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label"> Available Slots </label>

                <input
                  type="number"
                  min="0"
                  v-model.number="form.available_slots"
                  class="form-control"
                />
              </div>

              <div class="col-md-6 mb-3">
                <label class="form-label"> Booked Slots </label>

                <input class="form-control" :value="form.booked_slots" readonly />
              </div>

              <div class="col-md-6">
                <label class="form-label"> Status </label>

                <select v-model="form.status" class="form-select">
                  <option>Open</option>

                  <option>Closed</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Footer -->

          <div class="modal-footer">
            <button class="btn btn-cancel" type="button" @click="$emit('close')">Cancel</button>

            <button class="btn btn-save">Update Trek</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue'

import { updateTrek } from '@/services/staffService'

import { useToastStore } from '@/store/toast'

const toast = useToastStore()

const emit = defineEmits(['saved', 'close'])

const props = defineProps({
  show: Boolean,

  selectedTrek: Object,
})

const emptyForm = () => ({
  id: null,

  available_slots: 0,

  booked_slots: 0,

  status: 'Open',

  trek_name: '',

  location: '',

  difficulty: '',

  duration: 0,
})

const form = reactive(emptyForm())

watch(
  () => props.selectedTrek,

  (value) => {
    Object.assign(
      form,

      emptyForm(),
    )

    if (value) {
      Object.assign(
        form,

        value,
      )
    }
  },

  {
    immediate: true,
  },
)

async function save() {
  try {
    await updateTrek(
      form.id,

      {
        available_slots: form.available_slots,

        status: form.status,
      },
    )

    toast.success('Trek Updated')

    emit('saved')

    emit('close')
  } catch (err) {
    toast.error(err.response?.data?.message || 'Operation Failed')
  }
}
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
}

.modal-title {
  color: white;

  font-weight: 700;
}

.modal-header .btn-close {
  filter: invert(1);
}

.modal-body {
  padding: 28px;
}

.form-label {
  font-weight: 600;

  font-size: 0.9rem;

  margin-bottom: 6px;
}

.form-control,
.form-select {
  border-radius: 10px;

  padding: 10px;
}

.form-control:focus,
.form-select:focus {
  box-shadow: none;

  border-color: #184e37;
}

.modal-footer {
  padding: 18px 28px;
}

.btn-save {
  background: #184e37;

  color: white;

  border: none;

  border-radius: 10px;

  padding: 10px 20px;
}

.btn-save:hover {
  background: #133d2b;

  color: white;
}

.btn-cancel {
  border: 1px solid #ddd;

  border-radius: 10px;

  padding: 10px 20px;
}
</style>
