import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import AuthSystem from '../API/server';


const LoginComponent = ({user, setUser}) => {
  let [localData, setLocalData] = useState({
    username: '',
    email: '',
    password: '',
    access: '',
    refresh: '',
  });

  async function getSetTokens() {
    let result = await AuthSystem.getTokens({
      username: localData.username, 
      password: localData.password
    });
    await setLocalData({
      username: localData.username,
      email: result.email,
      password: localData.password,
      access: result.access,
      refresh: result.refresh,
    });
    await console.log(result);
    await setUser({
      username: localData.username,
      email: result.email,
      password: localData.password,
      access: result.access,
      refresh: result.refresh,
    });
  }

  useEffect(() => {
    console.log(localData);
  }, [localData]) 

  return (
    <div>
      <input type="text" onChange={(e) => setLocalData({username: e.target.value, password: localData.password, access: localData.access, refresh: localData.refresh})}/>
      <input type="password" onChange={(e) => setLocalData({username: localData.username, password:e.target.value, access: localData.access, refresh: localData.refresh})}/>
      <button onClick={getSetTokens}>Send</button>
    </div>
  );
};

export default LoginComponent;