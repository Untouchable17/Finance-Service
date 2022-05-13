import axios from 'axios';
import jwt_decode from "jwt-decode";

import {$authHost, $host} from "./index";


export const registration = async (email, username, password) => {

    const data = await $host.post("auth/sign-up/", {email, username, password})
    localStorage.setItem('token', data.data.access_token)
    const response_registration = {
        "token": jwt_decode(data.data.access_token),
        "other": data
    }

    return response_registration
}

export const login = async (username, password) => {

    const config = {
        headers: {'Content-Type': 'multipart/form-data'}
    };

    try {
        const data = await axios.post(`http://127.0.0.1:666/auth/sign-in/`, {username, password}, config)
        localStorage.setItem('token', data.data.access_token)
        const response_login = {
            "token": jwt_decode(data.data.access_token),
            "other": data
        }
        return response_login
    }
    catch (err) {
         return err
    }
}

export const check = async () => {
     const config = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `token: ${localStorage.getItem("token")}`
        }
     };

    const {data} = await $host.get("auth/validate", config)
    return data
}


