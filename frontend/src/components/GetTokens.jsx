import React, { useEffect, useState } from "react";
import AuthSystem from "../API/server";

function GetTokens({token, }) {
  let [jwtTokens, setJWTTokens] = useState([]);
  
  async function getResponse() {
    let user = {
      username: 'as',
      password: "as1as1as1",
    };
    let tokens = await AuthSystem.getTokens(user);
    await setJWTTokens([tokens.access, tokens.refresh]);
    //await setAccess(tokens.access);
    //await setRefresh(tokens.refresh);
    
  };
  
  useEffect(() => {
    getResponse();
  }, []);

  return (
    <div className="tokens"> 
    {jwtTokens[0]} <br/>
    {jwtTokens[1]}
    </div>
  );
}

export default GetTokens;
