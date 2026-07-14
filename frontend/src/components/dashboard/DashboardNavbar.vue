<template>

<div
class="bg-white shadow-sm rounded-4
d-flex justify-content-between
align-items-center p-3 mb-4">

<h3>

Admin Dashboard

</h3>

<div>

Welcome,

<b>

{{ auth.user?.name }}

</b>

</div>

</div>

</template>

<script setup>

import { useAuthStore } from "@/store/auth";

const auth=useAuthStore();

</script>