import React, { useEffect, useState } from "react";
import {BrowserRouter,Outlet,Route, Routes,} from "react-router-dom";
import { paths } from "./configure/pages";


function App() {
  let [user, setUser] = useState({
    username: '',
    email: '',
    password: '',
    access: '',
    refresh: '',
  });

  useEffect(() => {
    console.log(`user: ${user.access}`) 
  }, [user])
  return (
    <div>
      <BrowserRouter>
        <Routes>
          {paths.map(route => 
            <Route path={route.path} element={<route.component user={user} setUser={setUser}/>}/>
          )}
        </Routes>
      </BrowserRouter>
      <Outlet/>
    </div>
  );
}

export default App;