//export default class AuthSystem:
import axios from "axios";


export default class AuthSystem {
    static async getTokens(user){
          const resp = await axios.post("http://127.0.0.1:8000/auth/token/", user);
          const res = await resp.data;
          return res;
    };
    
    static async login(user){
        const resp = await axios.post('http://127.0.0.1:8000/auth/login/', user);
        const result = await resp.data;
        return result;
    };

    static async register(user){
        const resp = await axios.post('http://127.0.0.1:8000/auth/register/', user);
        const result = await resp.data;
        return result;    
    };
}