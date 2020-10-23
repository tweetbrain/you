import React from 'react';
// import './Navigation.css';

const Song = ({full_title}) => {
    return(
    <nav>
        <p className="f1">Song is {full_title} </p>
    </nav>
    ) 

}
export default Song;