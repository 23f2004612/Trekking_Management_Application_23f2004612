<template>
    <DashboardLayout>

        <div class="row mb-4">

            <div class="col-md-3">
                <StatCard
                    title="Treks"
                    :value="summary.total_treks"
                />
            </div>

            <div class="col-md-3">
                <StatCard
                    title="Users"
                    :value="summary.total_users"
                />
            </div>

            <div class="col-md-3">
                <StatCard
                    title="Staff"
                    :value="summary.total_staff"
                />
            </div>

            <div class="col-md-3">
                <StatCard
                    title="Bookings"
                    :value="summary.total_bookings"
                />
            </div>

        </div>

        <div class="row">

            <div class="col-lg-8 mb-4">

                <LineChart
                    :chartData="lineData"
                />

            </div>

            <div class="col-lg-4 mb-4">

                <PieChart
                    :chartData="pieData"
                />

            </div>

        </div>

    </DashboardLayout>
</template>

<script setup>

import { reactive, onMounted } from "vue";

import DashboardLayout from "@/components/dashboard/DashboardLayout.vue";
import StatCard from "@/components/dashboard/StatCard.vue";
import LineChart from "@/components/dashboard/LineChart.vue";
import PieChart from "@/components/dashboard/PieChart.vue";

import { getSummary } from "@/services/adminService";

const summary = reactive({

    total_treks: 0,
    total_users: 0,
    total_staff: 0,
    total_bookings: 0

});

const lineData = {

    labels: ["Jan","Feb","Mar","Apr"],

    datasets: [

        {

            label: "Bookings",

            data: [20,45,32,61]

        }

    ]

};

const pieData = {

    labels: ["Easy","Moderate","Hard"],

    datasets: [

        {

            data: [5,4,3]

        }

    ]

};

async function loadSummary(){

    try{

        const response = await getSummary();

        Object.assign(summary,response.data);

    }

    catch(err){

        console.error(err);

    }

}

onMounted(loadSummary);

</script>