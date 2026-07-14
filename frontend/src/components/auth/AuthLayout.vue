<template>

<div class="container-fluid min-vh-100">

    <div class="row min-vh-100">

        <!-- Left Panel -->

        <div
            class="col-lg-6 d-none d-lg-flex left-panel
            flex-column justify-content-center p-5">

            <div class="text-white">

                <h1 class="display-3 fw-bold">

                    Trailhead

                </h1>

                <p class="lead mt-4">

                    Manage treks, explore mountains,
                    and book your next adventure.

                </p>

            </div>

        </div>

        <!-- Right -->

        <div
            class="col-lg-6 d-flex
            justify-content-center
            align-items-center">

            <slot/>

        </div>

    </div>

</div>

</template>

<style scoped>

.left-panel{

    background:linear-gradient(
        135deg,
        #184E37,
        #2D6A4F
    );

}

</style>