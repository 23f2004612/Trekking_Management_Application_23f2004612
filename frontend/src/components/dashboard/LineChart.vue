<template>

<div class="card shadow-sm border-0">

    <div class="card-body">

        <Line
            :data="chartData"
            :options="options"
        />

    </div>

</div>

</template>

<script setup>

import {

Chart as ChartJS,
CategoryScale,
LinearScale,
PointElement,
LineElement,
Tooltip,
Legend

} from "chart.js";

import { Line } from "vue-chartjs";

ChartJS.register(

CategoryScale,
LinearScale,
PointElement,
LineElement,
Tooltip,
Legend

);

defineProps({

chartData:Object

});

const options={

responsive:true,

maintainAspectRatio:false

};

</script>

<style scoped>

.card{

height:350px;

}

</style>