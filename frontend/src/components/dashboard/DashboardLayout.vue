<template>

<div class="dashboard">

    <DashboardSidebar />

    <div class="main">

        <DashboardNavbar />

        <div class="content">

            <slot/>

        </div>

    </div>

</div>

</template>

<script setup>

import DashboardSidebar from "./DashboardSidebar.vue";
import DashboardNavbar from "./DashboardNavbar.vue";

</script>

<style scoped>

.dashboard{

    display:flex;

    min-height:100vh;

    background:#f7f7f5;

}

.main{

    flex:1;

}

.content{

    padding:30px;

}

</style>
