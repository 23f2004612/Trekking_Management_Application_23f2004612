<template>

<div class="input-group mb-4">

    <span class="input-group-text">

        <i class="bi bi-search"></i>

    </span>

    <input

        v-model="search"

        class="form-control"

        placeholder="Search treks..."

    >

</div>

</template>

<script setup>

import { ref, watch } from "vue";

const emit = defineEmits(["search"]);

const search = ref("");

watch(search,(value)=>{

    emit("search",value);

});

</script>