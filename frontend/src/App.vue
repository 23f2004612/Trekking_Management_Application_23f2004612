<template>

    <Navbar />

    <AppToast />

    <RouterView />

</template>

<script setup>

import { onMounted } from "vue";

import Navbar from "./components/layout/Navbar.vue";
import AppToast from "@/components/common/AppToast.vue";

import { currentUser } from "@/services/authService";

import { useAuthStore } from "@/store/auth";

const auth = useAuthStore();

onMounted(async()=>{

    auth.restoreFromStorage();

    try{

        const response = await currentUser();

        auth.setUser(response.data);

    }

    catch{

        auth.logout();

    }

});

</script>