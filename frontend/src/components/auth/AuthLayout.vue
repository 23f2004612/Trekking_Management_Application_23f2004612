<template>
  <div class="container-fluid min-vh-100">
    <div class="row min-vh-100">
      <!-- Left Panel -->
      <div
        class="col-lg-6 d-none d-lg-flex left-panel
            flex-column justify-content-center p-5"
      >
        <div class="photo-box mb-5">
          <img src="@/assets/images/trek-1.jpg" alt="Trekking in the mountains" />
        </div>

        <div class="text-white">
          <h1 class="display-3 fw-bold">Trailhead</h1>

          <p class="lead mt-4">Manage treks, explore mountains, and book your next adventure.</p>
        </div>
      </div>

      <!-- Right -->
      <div
        class="col-lg-6 d-flex right-panel
            justify-content-center
            align-items-center"
      >
        <slot />
      </div>
    </div>
  </div>
</template>

<style scoped>
.left-panel {
  background: linear-gradient(135deg, #184e37, #2d6a4f);
  position: relative;
  overflow: hidden;
}

.right-panel {
  background: #faf8f3;
}

.photo-box {
  background: #fff;
  padding: 10px 10px 26px;
  border-radius: 4px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
  transform: rotate(-4deg);
  width: 240px;
}

.photo-box img {
  width: 100%;
  height: 170px;
  object-fit: cover;
  display: block;
  border-radius: 2px;
}
</style>