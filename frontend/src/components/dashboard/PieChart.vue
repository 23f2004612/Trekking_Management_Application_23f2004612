<template>

<div class="card shadow-sm border-0">

<div class="card-body">

<Pie

:data="chartData"

/>

</div>

</div>

</template>

<script setup>

import {

Chart as ChartJS,

ArcElement,

Tooltip,

Legend

} from "chart.js";

import {

Pie

} from "vue-chartjs";

ChartJS.register(

ArcElement,

Tooltip,

Legend

);

defineProps({

chartData:Object

});

</script>

<style scoped>

.card{

height:350px;

}

</style>