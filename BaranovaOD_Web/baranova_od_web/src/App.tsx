import './App.css'
import { Card, useToaster } from "@gravity-ui/uikit";
import useWebSocket from "react-use-websocket";
import { useEffect } from "react";

function App() {

  const style = {
    width: '1280px',
    height: '700px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    overflow: 'hidden',
    background: "#000"
  }
  const { add } = useToaster();

  const { lastMessage } = useWebSocket("ws://localhost:8765/ws");

  useEffect(() => {
    add({
      name: "dangerous",
      title: lastMessage?.data,
      theme: "danger",
      autoHiding: false
    })
  }, [lastMessage]);



  return (
    <>
      <Card style={style} view="outlined" type="container" size="l">
        <img style={{ border: "none", objectFit: "contain", width: "100%" }} src={"http://localhost:5000"} />
      </Card>
    </>
  )
}

export default App
