<template>

<div class="card shadow-sm border-0">

<div class="card-body">

<p class="text-muted">

{{ title }}

</p>

<h2>

{{ value }}

</h2>

</div>

</div>

</template>

<script setup>

defineProps({

title:String,

value:[String,Number]

});

</script>