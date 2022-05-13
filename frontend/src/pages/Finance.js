import React, {useContext, useEffect, useState} from 'react';
import {Container, Col, Button, Row} from "react-bootstrap";
import Card from "react-bootstrap/Card";
import CardGroup from "react-bootstrap/CardGroup";
import {useParams, Link} from 'react-router-dom';
import {observer} from "mobx-react-lite";
import axios from 'axios';

import {fetchOperations} from '../http/FinanceAPI';
import {Context} from '../index';
import TypeBar from "../components/TypeBar";


const Finance = observer(( ) => {

    const [operations, setOperations] = useState([])
    useEffect(() => {
        fetchOperations().then(data => setOperations(data))
    }, [])

    return (
        <Container>
            <Row>
                <Col md={3} className="mt-2">
                    <TypeBar />
                </Col>
                <Col md={9}>
                    <h2>Транзакции</h2>
                    {operations.map(operation =>(
                        <div className="col-md-4" key={operation.id}>
                            <h4>{operation.title}</h4>
                            <p>{operation.amount}</p>
                            <p>{operation.id}</p>
                            <Link to={{pathname: `/finance/${operation.id}`, fromDashboard: false}}>Детальнее</Link>
                        </div>
                    ))}
                </Col>
            </Row>
        </Container>
    );
});

export default Finance;