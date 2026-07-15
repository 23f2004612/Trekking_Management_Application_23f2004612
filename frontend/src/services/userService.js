import api from "./api";

export function getTreks() {
    return api.get("/user/treks");
}

export function searchTreks(query) {
    return api.get("/user/search", {
        params: { query }
    });
}

export function bookTrek(id) {
    return api.post(`/user/book/${id}`);
}

export function bookingHistory() {
    return api.get("/user/history");
}

export function cancelBooking(id) {
    return api.delete(`/user/booking/${id}`);
}

export function exportBookings() {
    return api.post("/user/history/export");
}

export function exportStatus(taskId) {
    return api.get(`/user/export/${taskId}`);
}

export function getProfile() {
  return api.get("/user/profile");
}

export function updateProfile(data) {
  return api.put("/user/profile", data);
}