<template>

<div class="sidebar">

    <h3 class="logo">

        Trailhead

    </h3>

    <RouterLink
        to="/admin"
        class="menu">

        Dashboard

    </RouterLink>

    <RouterLink
        to="/admin/treks"
        class="menu">

        Treks

    </RouterLink>

    <RouterLink
        to="/admin/staff"
        class="menu">

        Staff

    </RouterLink>

    <RouterLink
        to="/admin/users"
        class="menu">

        Users

    </RouterLink>

</div>

</template>

<style scoped>

.sidebar{

    width:260px;

    background:#184E37;

    color:white;

    padding:35px;

}

.logo{

    margin-bottom:40px;

    font-weight:700;

}

.menu{

    display:block;

    color:white;

    padding:14px;

    border-radius:10px;

    margin-bottom:10px;

}

.menu:hover{

    background:#2D6A4F;

    color:white;

}

.router-link-active{

    background:#2D6A4F;

}

</style>