import React, { useEffect, useState } from "react";
import axios from "axios";

const Sub = () => {
  // useState 로 통신한데이터 상태관리
  // axios 통신
  // useEffect로 화면 처음 렌더링할때 통신하는 함수 호출
  // ui

  const [user, setUser] = useState();

  const getUser = () => {
    axios({
      method: "get",
      url: "http://localhost:8001/user/",
    })
      .then((response) => {
        if (response.status === 200) {
          setUser(response.data.content);
        }
      })
      .catch(() => {})
      .finally(() => {});
  };

  useEffect(() => {
    getUser();
  }, []);

  console.log(user);

  return (
    <div>
      <h1>{user.username}</h1>
      <h1>{user.score}</h1>
      <img
        style={{ width: "500px", height: "500px" }}
        src={`data:image/png;base64,${user.img}`}
        alt='tree'
      />
    </div>
  );
};

export default Sub;
