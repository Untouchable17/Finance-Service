import React from 'react';


const OperationButton = ({children, ...props}) => {
    return (
        <button {...props}>{children}</button>
    )

}

export default OperationButton;