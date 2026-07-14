import api from "./api"

export const getTreks=()=>api.get("/admin/treks")

export const createTrek=(data)=>api.post("/admin/treks",data)

export const updateTrek=(id,data)=>api.put(`/admin/treks/${id}`,data)

export const removeTrek=(id)=>api.delete(`/admin/treks/${id}`)

export const getStaff=()=>api.get("/admin/staff")

export const getUsers=()=>api.get("/admin/users")

export const getSummary=()=>api.get("/admin/summary")

export function searchTreks(query){
    return api.get("/admin/search",{
        params:{
           query
        }
    });
}
