<template>
  <div class="sidebar">
    <div class="brand">
      <h3 class="logo">Trailhead</h3>
      <small class="tagline">TREKKING MGMT</small>
    </div>

    <nav class="menu-group">
      <RouterLink to="/admin" class="menu">
        <i class="bi bi-speedometer2"></i>
        <span>Dashboard</span>
      </RouterLink>

      <RouterLink to="/admin/treks" class="menu">
        <i class="bi bi-signpost-split"></i>
        <span>Treks</span>
      </RouterLink>

      <RouterLink to="/admin/staff" class="menu">
        <i class="bi bi-person-badge"></i>
        <span>Staff</span>
      </RouterLink>

      <RouterLink to="/admin/users" class="menu">
        <i class="bi bi-people"></i>
        <span>Users</span>
      </RouterLink>
    </nav>
  </div>
</template>

<style scoped>
.sidebar {
  width: 260px;
  background: #184e37;
  color: white;
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
}

.brand {
  padding: 0 10px 30px;
  margin-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.logo {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 700;
  margin-bottom: 4px;
}

.tagline {
  letter-spacing: 1.8px;
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.6);
}

.menu-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.menu {
  display: flex;
  align-items: center;
  gap: 12px;
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  padding: 12px 14px;
  border-radius: 10px;
  font-weight: 500;
  font-size: 0.95rem;
  transition: background 0.2s ease, color 0.2s ease;
}

.menu i {
  font-size: 1.05rem;
}

.menu:hover {
  background: rgba(255, 255, 255, 0.08);
  color: white;
}

.router-link-active {
  background: #2d6a4f;
  color: white;
  font-weight: 600;
}
</style>