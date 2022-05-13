import { Container, Button, Navbar, Nav } from 'react-bootstrap';
import React, {useContext} from 'react';
import {observer} from "mobx-react-lite";
import {NavLink} from 'react-router-dom';

import {Context} from '../index';
import {LOGIN_ROUTE, REGISTRATION_ROUTE} from "../utils/consts";


const NavBar = observer(() => {

    const {user} = useContext(Context);
    const logout = () => {
        user.setUser({})
        user.setIsAuth(false)
    }

    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="#home">Navbar</Navbar.Brand>
                {user.isAuth ?
                    <Nav className="me-left">
                        <Button className="me-2" variant={"outline-light"}>Админ панель</Button>
                        <Button variant={"outline-light"} onClick={() => logout()}>Выйти</Button>
                    </Nav>
                :
                    <Nav className="me-left">
                        <Button className="me-2" variant={"light"}><NavLink to={LOGIN_ROUTE} style={{ textDecoration: 'none', color: '#000'}}>Войти</NavLink></Button>
                        <Button variant={"light"}><NavLink to={REGISTRATION_ROUTE} style={{ textDecoration: 'none', color: '#000'}}>Регистрация</NavLink></Button>
                    </Nav>
                }
            </Container>
        </Navbar>
    );
});

export default NavBar;