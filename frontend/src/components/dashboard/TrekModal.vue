<template>
  <div class="modal fade" id="trekModal" tabindex="-1">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <form @submit.prevent="saveTrek">
          <!-- Header -->

          <div class="modal-header">
            <h5 class="modal-title">
              {{ form.id ? 'Edit Trek' : 'Add Trek' }}
            </h5>

            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>

          <!-- Body -->

          <div class="modal-body">
            <div class="row">
              <!-- Trek Name -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Trek Name </label>

                <input v-model="form.trek_name" class="form-control" required />
              </div>

              <!-- Location -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Location </label>

                <input v-model="form.location" class="form-control" required />
              </div>

              <!-- Difficulty -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Difficulty </label>

                <select v-model="form.difficulty" class="form-select">
                  <option value="Easy">Easy</option>
                  <option value="Moderate">Moderate</option>
                  <option value="Hard">Hard</option>
                </select>
              </div>

              <!-- Duration -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Duration (Days) </label>

                <input type="number" min="1" v-model.number="form.duration" class="form-control" />
              </div>

              <!-- Available Slots -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Available Slots </label>

                <input
                  type="number"
                  min="1"
                  v-model.number="form.available_slots"
                  class="form-control"
                />
              </div>

              <!-- Staff -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Assign Staff </label>

                <select v-model="form.assigned_staff_id" class="form-select">
                  <option :value="null">Select Staff</option>

                  <option v-for="staff in staffList" :key="staff.id" :value="staff.id">
                    {{ staff.full_name }}
                  </option>
                </select>
              </div>

              <!-- Start Date -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> Start Date </label>

                <input type="date" v-model="form.start_date" class="form-control" />
              </div>

              <!-- End Date -->

              <div class="col-md-6 mb-3">
                <label class="form-label"> End Date </label>

                <input type="date" v-model="form.end_date" class="form-control" />
              </div>

              <!-- Description -->

              <div class="col-12">
                <label class="form-label"> Description </label>

                <textarea rows="4" v-model="form.description" class="form-control"> </textarea>
              </div>
            </div>
          </div>

          <!-- Footer -->

          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>

            <button class="btn btn-success">
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
import { useToastStore } from "@/store/toast";
import { Modal } from 'bootstrap'

const toast=useToastStore();

const emit = defineEmits(['saved'])

const props = defineProps({
  selectedTrek: Object,
})

const emptyForm = () => ({
  id: null,
  trek_name: '',
  location: '',
  difficulty: 'Easy',
  duration: 1,
  description: '',
  available_slots: 1,
  start_date: '',
  end_date: '',
  assigned_staff_id: null,
})

const form = reactive(emptyForm())

const staffList = ref([])

watch(
  () => props.selectedTrek,
  (value) => {
    Object.assign(form, emptyForm())

    if (value) {
      Object.assign(form, value)
    }
  },
  {
    immediate: true,
  },
)

async function loadStaff() {
  try {
    const response = await getStaff()

    staffList.value = response.data
  } catch (err) {
    console.error(err)
  }
}

async function saveTrek() {
  try {
    if (form.id) {
      await updateTrek(form.id, form)
      toast.success("Trek Updated");
    } else {
      await createTrek(form)
      toast.success("Trek Created");
    }

    emit('saved')

    const modal = bootstrap.Modal.getInstance(document.getElementById('trekModal'))

    modal.hide()
  } catch (err) {
    toast.error(

err.response?.data?.message ||

"Operation Failed"

);
  }
}

onMounted(loadStaff)
</script>
