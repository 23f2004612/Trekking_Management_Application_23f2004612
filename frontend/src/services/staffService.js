import api from "./api";

export function assignedTreks(){

    return api.get("/staff/treks");

}

export function trekBookings(id){

    return api.get(`/staff/treks/${id}`);

}

export function updateBooking(id,status){

    return api.put(`/staff/booking/${id}`,{

        booking_status:status

    });

}

export function getProfile(){

    return api.get("/staff/profile");

}

export function updateProfile(data){

    return api.put("/staff/profile",data);

}