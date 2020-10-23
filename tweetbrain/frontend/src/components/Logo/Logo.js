import React from 'react';
import Tilt from 'react-tilt';
import './Logo.css';
import twitter from './twitter.png';

const Logo = () => {
    return(
        <div className="">
            <Tilt className="Tilt br2 shadow-2 center" options={{ max : 30 }} style={{ height: 220, width: 220 }} >
                <div className="Tilt-inner pa5"><img src={twitter}></img></div>
            </Tilt>
        </div>
    ) 
}
export default Logo;