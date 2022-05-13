import React, {useContext, useState, useEffect} from 'react';
import {useForm} from 'react-hook-form';
import {ListGroup} from "react-bootstrap";
import {observer} from 'mobx-react-lite';

import OperationButton from "./UI/button/OperationButton";
import OperationInput from "./UI/input/OperationInput";
import { fetchOneUpdateOperation } from '../http/FinanceAPI';
import {Context} from "../index";

const TypeBar = observer(() => {

    const [operations, setOperations] = useState([])
    const [operation, setOperation] = useState(
        {date: '', kind: '', amount: '', description: ''}
    )

    const addNewOperation = (e) => {
        e.preventDefault()

        useEffect(() => {
            fetchOneUpdateOperation().then(data => setOperations(...operations))
        }, [])
    }

    return (
        <ListGroup>
             <hr />
             <h2>Создать транзакцию</h2>
            <form action=''>
                <OperationInput type="date" value={operation.date} onChange={e => setOperation({...operation, date: e.target.value})} /><br/>
                <OperationInput type="text" value={operation.kind} onChange={e => setOperation({...operation, kind: e.target.value})} placeholder="kind"/><br/>
                <OperationInput type="text" value={operation.amount} onChange={e => setOperation({...operation, amount: e.target.value})} placeholder="amount" /><br/>
                <OperationInput type="text" value={operation.description} onChange={e => setOperation({...operation, description: e.target.value})} placeholder="description" /><br/>
                <OperationButton onClick={addNewOperation}>Создать</OperationButton>
            </form>
        </ListGroup>
    );
});

export default TypeBar;
