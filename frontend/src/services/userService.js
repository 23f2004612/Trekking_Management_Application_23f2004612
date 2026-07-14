import api from "./api";

export function getTreks(){

    return api.get("/user/treks");

}

export function bookTrek(id){

    return api.post(`/user/book/${id}`);

}

export function bookingHistory(){

    return api.get("/user/bookings");
}

export function exportHistory(taskId){
    return api.get(`/user/export/${taskId}`);
}