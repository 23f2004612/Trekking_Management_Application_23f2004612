import api from "./api";

// ---------------- Dashboard ----------------

export const getDashboard = () =>
    api.get("/admin/dashboard");

// ---------------- Treks ----------------

export const getTreks = () =>
    api.get("/admin/treks");

export const createTrek = (data) =>
    api.post("/admin/treks", data);

export const updateTrek = (id, data) =>
    api.put(`/admin/treks/${id}`, data);

export const removeTrek = (id) =>
    api.delete(`/admin/treks/${id}`);

export const searchTreks = (query) =>
    api.get("/admin/search/treks", {
        params: { query }
    });

// ---------------- Staff ----------------

export const getStaff = () =>
    api.get("/admin/staff");

export const createStaff = (data) =>
    api.post("/admin/staff", data);

export const updateStaff = (id, data) =>
    api.put(`/admin/staff/${id}`, data);

export const removeStaff = (id) =>
    api.delete(`/admin/staff/${id}`);

export const searchStaff = (query) =>
    api.get("/admin/search/staff", {
        params: { query }
    });

// ---------------- Users ----------------

export const getUsers = () =>
    api.get("/admin/users");

export const searchUsers = (query) =>
    api.get("/admin/search/users", {
        params: { query }
    });

export const updateUserStatus = (id, status) =>
    api.put(`/admin/users/${id}/status`, {
        status
    });