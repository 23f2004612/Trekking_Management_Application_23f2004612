<template>

<section class="container py-5">

    <div
        class="d-flex justify-content-between align-items-center mb-5"
    >

        <div>

            <h2 class="section-title">

                Featured Treks

            </h2>

            <p class="text-muted">

                Discover our most popular trekking experiences.

            </p>

        </div>

    </div>

    <div
        v-if="loading"
        class="text-center"
    >

        <div
            class="spinner-border text-success"
        ></div>

    </div>

    <div
        v-else
        class="row"
    >

        <div
            class="col-lg-4 mb-4"
            v-for="trek in treks"
            :key="trek.id"
        >

            <TrekCard
                :trek="trek"
            />

        </div>

    </div>

</section>

</template>

<script setup>

import { ref,onMounted } from "vue";

import TrekCard from "../trek/TrekCard.vue";

import { getAvailableTreks } from "@/services/trekService";

const treks=ref([]);

const loading=ref(true);

async function loadTreks(){

    try{

        const response=await getAvailableTreks();

        treks.value=response.data;

    }

    catch(err){
        console.log(err);
    }

    finally{
        loading.value=false;
    }

}

onMounted(loadTreks);

</script>
