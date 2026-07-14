import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import { useAuthStore } from "@/store/auth";
import AdminDashboard from "@/views/admin/Dashboard.vue";
import Treks from "@/views/admin/Treks.vue";
import StaffDashboard from "@/views/staff/Dashboard.vue";
import { currentUser } from "@/services/authService";

const Dummy = {
    template:"<div class='container mt-5'><h2>Coming Soon...</h2></div>"
};

const routes = [
    {
        path: "/",
        name: "home",
        component: Home
    },

    {
        path: "/login",
        name: "login",
        component: Login
    },

    {
        path: "/register",
        name: "register",
        component: Register
    },
    {
        path:"/browse",
        component:Dummy
    },

    {
        path:"/bookings",
        component:Dummy
    },
    {
        path:"/admin",
        component:AdminDashboard,
        meta: { requiresAuth: true, requiredRole: "admin" }
    },
    {
        path:"/admin/treks",
        component:Treks,
        meta: { requiresAuth: true, requiredRole: "admin" }
    },
    {
        path:"/staff",
        component:StaffDashboard,
        meta: { requiresAuth: true, requiredRole: "staff" }
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

// Flag to track if initial auth restore is done
let authRestoreDone = false;

router.beforeEach(async (to, from, next) => {
    const auth = useAuthStore();

    // Restore auth from localStorage first (immediate)
    if (!authRestoreDone) {
        auth.restoreFromStorage();
        
        // Try to verify session with server
        try {
            const response = await currentUser();
            auth.setUser(response.data);
        } catch (err) {
            // Session is invalid, clear auth state
            auth.logout();
        }
        authRestoreDone = true;
    }

    // Check route protection
    if (to.meta.requiresAuth) {
        if (!auth.loggedIn) {
            return next("/login");
        }
        
        if (to.meta.requiredRole && auth.role !== to.meta.requiredRole) {
            return next("/login");
        }
    }

    next();
});

export default router;