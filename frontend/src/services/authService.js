import api from './api'

export function loginUser(data) {
  return api.post('/login', data)
}

export function logoutUser() {
  return api.post('/logout')
}

export function currentUser() {
  return api.get('/me')
}

export function registerUser(data){
    return api.post("/register",data);
}

