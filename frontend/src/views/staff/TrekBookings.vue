<template>
  <DashboardLayout>

    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2>Trek Bookings</h2>

      <RouterLink
        to="/staff"
        class="btn btn-outline-success"
      >
        Back
      </RouterLink>
    </div>

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="bookings.length===0"
      title="No Bookings Found"
    />

    <div v-else class="card">

      <div class="table-responsive">

        <table class="table align-middle mb-0">

          <thead>

            <tr>
              <th>User</th>
              <th>Email</th>
              <th>Booking Date</th>
              <th>Status</th>
              <th width="170">Action</th>
            </tr>

          </thead>

          <tbody>

            <tr
              v-for="booking in bookings"
              :key="booking.id"
            >

              <td>{{ booking.user.full_name }}</td>

              <td>{{ booking.user.email }}</td>

              <td>{{ booking.booking_date }}</td>

              <td>

                <span
                  class="badge"
                  :class="{
                    'bg-success':booking.booking_status==='Booked',
                    'bg-primary':booking.booking_status==='Completed',
                    'bg-danger':booking.booking_status==='Cancelled'
                  }"
                >
                  {{ booking.booking_status }}
                </span>

              </td>

              <td>

                <select
                  class="form-select"
                  v-model="booking.booking_status"
                  @change="changeStatus(booking)"
                >

                  <option>Booked</option>

                  <option>Completed</option>

                  <option>Cancelled</option>

                </select>

              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </DashboardLayout>
</template>

<script setup>

import { ref,onMounted } from "vue";

import { useRoute } from "vue-router";

import DashboardLayout from "@/components/dashboard/DashboardLayout.vue";

import Loader from "@/components/common/Loader.vue";

import EmptyState from "@/components/common/EmptyState.vue";

import {

    trekBookings,

    updateBooking

} from "@/services/staffService";

const route=useRoute();

const bookings=ref([]);

const loading=ref(false);

async function loadBookings(){

    loading.value=true;

    const res=await trekBookings(route.params.id);

    bookings.value=res.data;

    loading.value=false;

}

async function changeStatus(booking){

    await updateBooking(

        booking.id,

        booking.booking_status

    );

}

onMounted(loadBookings);

</script>