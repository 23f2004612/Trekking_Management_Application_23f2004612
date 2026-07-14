<template>

<DashboardLayout>

    <h2 class="mb-4">

        Assigned Treks

    </h2>

    <DataTable

        :treks="treks"

        @edit="updateStatus"

    />

</DashboardLayout>

</template>

<script setup>

import { ref,onMounted } from "vue";

import DashboardLayout from "@/components/dashboard/DashboardLayout.vue";

import DataTable from "@/components/dashboard/DataTable.vue";

import { getAssignedTreks } from "@/services/staffService";

const treks = ref([]);

async function loadTreks(){
    const res = await getAssignedTreks();
    treks.value = res.data;
}

function updateStatus(trek){
    console.log(trek);
}

onMounted(loadTreks);

</script>