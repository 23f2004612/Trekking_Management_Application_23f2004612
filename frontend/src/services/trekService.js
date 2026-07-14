import api from "./api";

export function getAvailableTreks(){
    return api.get("/user/treks");
}

export function getTrek(id){
    return api.get(`/user/treks/${id}`);
}