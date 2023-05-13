import React from "react";
import './App.scss';
import FormApiCall from "./formApiCall";

function App() {
  return <>
    <h1 className="app-title">Docx-Analyser</h1> {/* Added 'app-title' class here */}
    <FormApiCall/>
  </>;
}

export default App;
