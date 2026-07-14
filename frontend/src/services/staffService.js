import api from "./api";

export function getAssignedTreks(){

    return api.get("/staff/treks");

}

export function updateStatus(id,data){

    return api.put(`/staff/treks/${id}`,data);

}

export function getBookings(id){

    return api.get(`/staff/bookings/${id}`);

}