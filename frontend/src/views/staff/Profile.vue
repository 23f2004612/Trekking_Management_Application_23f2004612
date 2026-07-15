<template>
  <DashboardLayout>

    <div class="row justify-content-center">

      <div class="col-lg-7">

        <div class="card shadow-sm">

          <div class="card-header">
            <h4 class="mb-0">My Profile</h4>
          </div>

          <div class="card-body">

            <form @submit.prevent="save">

              <div class="mb-3">

                <label class="form-label">Full Name</label>

                <input
                  class="form-control"
                  v-model="form.full_name"
                >

              </div>

              <div class="mb-3">

                <label class="form-label">Email</label>

                <input
                  class="form-control"
                  v-model="form.email"
                  disabled
                >

              </div>

              <div class="mb-3">

                <label class="form-label">Phone</label>

                <input
                  class="form-control"
                  v-model="form.contact_number"
                >

              </div>

              <div class="mb-3">

                <label class="form-label">Specialization</label>

                <input
                  class="form-control"
                  v-model="form.specialization"
                >

              </div>

              <div class="mb-3">

                <label class="form-label">Experience</label>

                <input
                  type="number"
                  class="form-control"
                  v-model="form.experience"
                >

              </div>

              <button
                class="btn btn-success"
              >
                Save Changes
              </button>

            </form>

          </div>

        </div>

      </div>

    </div>

  </DashboardLayout>
</template>

<script setup>

import { reactive,onMounted } from "vue";

import DashboardLayout from "@/components/dashboard/DashboardLayout.vue";

import {

    getProfile,

    updateProfile

} from "@/services/staffService";

const form=reactive({

    full_name:"",

    email:"",

    contact_number:"",

    specialization:"",

    experience:0

});

async function load(){

    const res=await getProfile();

    Object.assign(form,res.data);

}

async function save(){

    await updateProfile(form);

}

onMounted(load);

</script>