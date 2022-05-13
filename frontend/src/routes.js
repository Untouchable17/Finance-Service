import Admin from "./pages/Admin";
import Auth from "./pages/Auth";
import Finance from "./pages/Finance";
import FinanceDetail from "./pages/FinanceDetail";
import {
    ADMIN_ROUTE,
    LOGIN_ROUTE,
    REGISTRATION_ROUTE,
    FINANCE_ROUTE,
    FINANCE_DETAIL_ROUTE
} from "./utils/consts";


export const authRoutes = [
    {
        path: ADMIN_ROUTE,
        Component: Admin
    },
]

export const publicRoutes = [
    {
        path: LOGIN_ROUTE,
        Component: Auth
    },
    {
        path: REGISTRATION_ROUTE,
        Component: Auth
    },
    {
        path: FINANCE_ROUTE,
        Component: Finance
    },
    {
        path: FINANCE_DETAIL_ROUTE + '/:id',
        Component: FinanceDetail
    },
]