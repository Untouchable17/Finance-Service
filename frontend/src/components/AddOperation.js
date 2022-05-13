import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';


const AddOperation = (props) => {
    const [operation, setOperation] = useState({});

    useEffect(() => {
        const operation_id = props.match.params.id;

        const fetchData = async () => {
            try {
                const res = await axios.get(`http://127.0.0.1:666/operations/${operation_id}`);
                setOperation(res.data);
            } catch (e) {

            }
        };

        fetchData();
    }, [props.match.id]);

    const createOperation = () => {
        return {__html: operation.content}
    }

    return (
        <div className="container mt-3">
            <h1>{operation.amount}</h1>
            <h2>category</h2>
            <h4>date</h4>
            <div className="mt-5 mb-5" dangerousSetInnerHTML={createOperation()}/>
            <p><Link to="/finance">Back to operations</Link></p>
        </div>
    )
}

export default AddOperation;