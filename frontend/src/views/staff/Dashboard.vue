<template>
  <DashboardLayout>

    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2>Assigned Treks</h2>
    </div>

    <Loader v-if="loading" />

    <EmptyState
      v-else-if="treks.length===0"
      title="No Treks Assigned"
    />

    <div v-else class="row">

      <div
        class="col-lg-4 mb-4"
        v-for="trek in treks"
        :key="trek.id"
      >

        <TrekCard
          :trek="trek"
          :showActions="false"
        />

        <div class="card border-top-0">

          <div class="card-body">

            <p>
              <strong>Booked :</strong>

              {{ trek.booked_slots }}/{{ trek.available_slots }}
            </p>

            <RouterLink
              class="btn btn-success w-100"
              :to="`/staff/trek/${trek.id}`"
            >
              View Bookings
            </RouterLink>

          </div>

        </div>

      </div>

    </div>

  </DashboardLayout>
</template>

<script setup>

import { ref,onMounted } from "vue";

import DashboardLayout from "@/components/dashboard/DashboardLayout.vue";
import Loader from "@/components/common/Loader.vue";
import EmptyState from "@/components/common/EmptyState.vue";
import TrekCard from "@/components/trek/TrekCard.vue";

import { assignedTreks } from "@/services/staffService";

const loading = ref(false);

const treks = ref([]);

async function loadTreks(){

    loading.value=true;

    const res = await assignedTreks();

    treks.value=res.data;

    loading.value=false;

}

onMounted(loadTreks);

</script>