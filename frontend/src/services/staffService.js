import api from "./api";

export function getDashboard() {
  return api.get("/staff/dashboard");
}

export function getAssignedTreks() {
  return api.get("/staff/my-treks");
}

export function updateTrek(id, data) {
  return api.put(`/staff/treks/${id}`, data);
}

export function getParticipants(id) {
  return api.get(`/staff/treks/${id}/participants`);
}

export function completeTrek(id) {
  return api.put(`/staff/treks/${id}/complete`);
}