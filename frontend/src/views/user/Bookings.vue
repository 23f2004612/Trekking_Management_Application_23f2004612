<template>
  <div class="container py-5">

    <div class="d-flex justify-content-between align-items-center mb-4">

      <h2>My Bookings</h2>

      <button
        class="btn btn-success"
        @click="exportHistory"
      >
        Export CSV
      </button>

    </div>

    <div
      v-if="bookings.length === 0"
      class="alert alert-light text-center"
    >
      You haven't booked any treks yet.
    </div>

    <div
      v-else
      class="row"
    >

      <div
        class="col-md-6 mb-4"
        v-for="booking in bookings"
        :key="booking.id"
      >

        <TrekCard
          :trek="booking.trek"
          :guest="!auth.loggedIn"
        />

        <div class="card border-top-0 rounded-top-0">

          <div class="card-body">

            <div class="mb-2">

              <strong>Status :</strong>

              <span
                class="badge ms-2"
                :class="badgeClass(booking.booking_status)"
              >
                {{ booking.booking_status }}
              </span>

            </div>

            <div class="mb-3">

              <strong>Booked On :</strong>

              {{ booking.booking_date }}

            </div>

            <button
              v-if="booking.booking_status==='Booked'"
              class="btn btn-outline-danger btn-sm"
              @click="cancelBookingHandler(booking.id)"
            >
              Cancel Booking
            </button>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>

import { ref,onMounted } from "vue";

import TrekCard from "@/components/trek/TrekCard.vue";

import {
    bookingHistory,
    cancelBooking,
    exportBookings,
    exportStatus
} from "@/services/userService";
import { useAuthStore } from "@/store/auth";

const auth = useAuthStore();

async function exportHistory(){

    const res = await exportBookings();

    const taskId = res.data.task_id;

    const interval = setInterval(async()=>{

        const status = await exportStatus(taskId);

        if(status.data.state==="SUCCESS"){

            clearInterval(interval);

            window.open(
                "http://localhost:5000/" + status.data.file,
                "_blank"
            );

        }

        if(status.data.state==="FAILURE"){

            clearInterval(interval);

            alert("Export failed.");

        }

    },1500);

}
const bookings = ref([]);

async function loadBookings(){

    const res = await bookingHistory();

    bookings.value = res.data;

}

async function cancelBookingHandler(id){

    await cancelBooking(id);

    loadBookings();

}

function badgeClass(status){

    return{

        "bg-success":status==="Booked",

        "bg-danger":status==="Cancelled",

        "bg-primary":status==="Completed"

    };

}

onMounted(loadBookings);

</script>