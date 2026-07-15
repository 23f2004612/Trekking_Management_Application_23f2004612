import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth",{

    state:()=>({

        user:null,

        loggedIn:false,

        role:null,

        isRestoring: true

    }),

    actions:{

        setUser(user){

            if (!user) {
                this.logout();
                return;
            }

            this.user = user;
            this.role = user.role;
            this.loggedIn = true;

            localStorage.setItem(
                "authUser",
                JSON.stringify(user)
            );
        },   

        logout(){

            this.user=null;
            this.role=null;
            this.loggedIn=false;

            // Clear localStorage
            localStorage.removeItem('authUser');

        },

        restoreFromStorage(){

            const stored = localStorage.getItem('authUser');

            if(stored){

                try{

                    const user = JSON.parse(stored);

                    this.user = user;

                    this.role = user.role;

                    this.loggedIn = true;

                }catch(e){

                    localStorage.removeItem('authUser');

                }

            }

            this.isRestoring = false;

        }

    }

});