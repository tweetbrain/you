import React from 'react';


const Song = ({full_title, image_url}) => {
    return(
    <nav>
        <p className="f1">Song:  {full_title} </p>
        <img src={image_url} style={{height: 500, width: 500, margin: 20}}></img>
    </nav>
    ) 

}
export default Song;