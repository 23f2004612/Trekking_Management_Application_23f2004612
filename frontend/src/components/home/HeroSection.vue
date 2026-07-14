<script setup>
    import heroImage from "@/assets/images/hero.jpg";
</script>

<template>
<section class="hero"
        :style="{
            backgroundImage: `linear-gradient(rgba(0,0,0,.45), rgba(0,0,0,.45)), url(${heroImage})`
            }"
>
    <div class="overlay">

        <div class="container h-100 d-flex align-items-center">

            <div class="hero-content">

                <span class="badge rounded-pill bg-light text-dark px-3 py-2">

                    <i class="bi bi-geo-alt"></i>

                    6 curated trails this season

                </span>

                <h1 class="display-2 fw-bold mt-4">

                    Book trails.

                    <br>

                    Chase altitude.

                </h1>

                <p class="lead mt-4">

                    A unified platform for trekkers, staff, and organizers
                    to manage routes, slots and adventures.

                </p>

                <div class="mt-4">

                    <RouterLink to="/browse" class="btn btn-warning btn-lg me-3">
                        Browse Treks
                    </RouterLink>

                    <RouterLink to="/register" class="btn btn-outline-light btn-lg">
                        Create Account
                    </RouterLink>
                </div>

            </div>

        </div>

    </div>

</section>

</template>

<style scoped>

.hero{

    height: 90vh;
    background-size: cover;
    background-position: center;
}

.overlay{

    height:100%;

}

.hero-content{

    color:white;

    max-width:700px;

}

.hero h1{

    font-size:5rem;

    line-height:1.1;

}

.hero p{

    max-width:600px;

    font-size:1.35rem;

}
</style>
