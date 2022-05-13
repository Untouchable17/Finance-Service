import React, {useEffect, useState} from 'react';
import {useParams, Link} from 'react-router-dom'
import {observer} from 'mobx-react-lite';
import axios from 'axios';

import {fetchOneOperation} from "../http/FinanceAPI";


const FinanceDetail = observer(( ) => {

    const [operation, setOperation] = useState({info: []})
    const {id} = useParams()
    useEffect(() => {
        fetchOneOperation(id).then(data => setOperation(data))
    }, [])

    console.log(operation)

    return (
        <div className="finance_detail">
            finance detail page
            <h2>{operation.kind}</h2>
            <h2>{operation.amount}</h2>
            <h2>{operation.description}</h2>
            <h2>{operation.date}</h2>
        </div>
    );
});

export default FinanceDetail;