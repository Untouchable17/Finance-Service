import React, {useContext} from "react";
import {Routes, Route, Redirect} from "react-router-dom";

import {authRoutes, publicRoutes} from "../routes";
import {Context} from "../index";


const AppRouter = () => {
    const {user} = useContext(Context)
    console.log(user)

    return (
        <Routes>
            {user.isAuth && authRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component />}/>
            )}
            {publicRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component />}/>
            )}
        </Routes>
    );
};

export default AppRouter;