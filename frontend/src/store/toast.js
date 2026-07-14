import { defineStore } from "pinia";

export const useToastStore = defineStore("toast",{

    state:()=>({

        show:false,
        message:"",
        type:"success",
        timeoutId:null

    }),

    actions:{

        success(message){

            if (this.timeoutId) clearTimeout(this.timeoutId);
            this.type="success";
            this.message=message;
            this.show=true;

            this.timeoutId = setTimeout(()=>{

                this.show=false;

            },3000);

        },

        error(message){

            if (this.timeoutId) clearTimeout(this.timeoutId);
            this.type="danger";
            this.message=message;
            this.show=true;

            this.timeoutId = setTimeout(()=>{

                this.show=false;

            },3000);

        }

    }

});