import React, { useEffect, useState } from "react";

function Temp({user}) {
  console.log(user)
  return (
    <div className="asd"> 
      {user.username}<br/>
      {user.email}<br/>
      {user.password}<br/>
      {user.access}<br/>
      {user.refresh}<br/>
    </div>
  );
}

export default Temp;
