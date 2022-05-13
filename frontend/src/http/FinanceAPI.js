import jwt_decode from "jwt-decode";
import axios from 'axios';

import {$authHost, $host} from "./index";


export const createOperation = async () => {
    const {data} = await $authHost.post("operations/", {})
    return data
}

export const fetchOperations = async () => {
     const config = {
        headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTIxMTgwMDMsIm5iZiI6MTY1MjExODAwMywiZXhwIjoxNjUyMTIxNjAzLCJzdWIiOiIxIiwidXNlciI6eyJlbWFpbCI6InR5bGVyYmxhY2tvdXQxN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNlY2RldDE3IiwiaWQiOjF9fQ.xZbTig2qm4NxiXWZYZoNYPh5-h5hv1OVPLtVGsYWbDg'
            }
        };

    const {data} = await $host.get("operations/", config)
    console.log(`Operations: ${data}`)
    return data
}

export const fetchOneOperation = async (id) => {
     const config = {
        headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTIxMTgwMDMsIm5iZiI6MTY1MjExODAwMywiZXhwIjoxNjUyMTIxNjAzLCJzdWIiOiIxIiwidXNlciI6eyJlbWFpbCI6InR5bGVyYmxhY2tvdXQxN0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6InNlY2RldDE3IiwiaWQiOjF9fQ.xZbTig2qm4NxiXWZYZoNYPh5-h5hv1OVPLtVGsYWbDg'
            }
        };

    const {data} = await $host.get(`operations/` + id, config)
    console.log(`Get one operation: ${data}`)
    return data
}




