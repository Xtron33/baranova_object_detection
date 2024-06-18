import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import '@gravity-ui/uikit/styles/fonts.css';
import '@gravity-ui/uikit/styles/styles.css';
import {ThemeProvider, ToasterComponent, ToasterProvider} from "@gravity-ui/uikit";



ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
      <ThemeProvider theme="light" >
          <ToasterProvider>
              <App />
              <ToasterComponent mobile={true}/>
          </ToasterProvider>
      </ThemeProvider>
  </React.StrictMode>,
)
