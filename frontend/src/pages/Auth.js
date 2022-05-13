import React, {useState, useContext} from 'react';
import {Container, Form, Button, Row} from "react-bootstrap";
import { NavLink, useLocation, useNavigate } from 'react-router-dom';
import Card from "react-bootstrap/Card";
import {observer} from "mobx-react-lite";

import {
    LOGIN_ROUTE,
    REGISTRATION_ROUTE,
    FINANCE_ROUTE
} from "../utils/consts";
import {registration, login} from "../http/userAPI";
import {Context} from '../index';


const Auth = observer(( ) => {

    const location = useLocation()
    const navigate = useNavigate()
    const {user} = useContext(Context)
    const isLogin = location.pathname === LOGIN_ROUTE

    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const click = async (props) => {
        try {
            if (isLogin){
                let data = await login(username, password);
                if (data.other.status === 200){
                    user.setUser(user);
                    user.setIsAuth(true);
                    navigate(FINANCE_ROUTE);
                } else {console.log("Ошибка при авторизации");}
            } else {
                let data = await registration(email, username, password);
                if (data.other.status === 200) {
                    user.setUser(user);
                    user.setIsAuth(true);
                    navigate(FINANCE_ROUTE);
                } else {
                    console.log("Ошибка при регистрации");
                }

            }
        } catch(e) {
            alert(e);
        }
    }

    return (
        <Container className="d-flex justify-content-center align-items-center" style={{height: window.innerHeight - 54}}>
            <Card style={{width: 600}} className="p-5">
                <h2 className="m-auto">{isLogin ? 'Авторизация' : "Регистрация"}</h2>
                <Form className="d-flex flex-column">
                    {isLogin ?
                        <div className="login__block">
                            <Form.Control
                                className="mt-3"
                                placeholder="Введите никнейм"
                                value={username}
                                onChange={e => setUsername(e.target.value)}
                            />
                            <Form.Control
                                className="mt-3"
                                placeholder="Введите пароль"
                                value={password}
                                onChange={e => setPassword(e.target.value)}
                                type="password"
                            />
                        </div>
                    :
                        <div className="registration__block">
                            <Form.Control
                                className="mt-3"
                                placeholder="Введите свою почту"
                                value={email}
                                onChange={e => setEmail(e.target.value)}
                            />
                            <Form.Control
                                className="mt-3"
                                placeholder="Желаемый никнейм"
                                value={username}
                                onChange={e => setUsername(e.target.value)}
                            />
                            <Form.Control
                                className="mt-3"
                                placeholder="Придумайте пароль"
                                value={password}
                                onChange={e => setPassword(e.target.value)}
                            />
                        </div>
                    }

                    <Row className="d-flex justify-content-between mt-3 pl-3 pr-3">
                        {isLogin ?
                            <div>Нет аккаунта? <NavLink to={REGISTRATION_ROUTE}>Зарегистрироваться</NavLink></div>
                            :
                            <div>Есть аккаунт? <NavLink to={LOGIN_ROUTE}>Войти</NavLink></div>
                        }
                        <Button variant={"outline-success"} onClick={click}>
                            {isLogin ? 'Войти' : 'Регистрация'}
                        </Button>
                    </Row>

                </Form>
            </Card>

        </Container>
    );
});

export default Auth;
