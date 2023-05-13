import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';
import React, { useState } from 'react';
import './FormApiCall.css'; 
import { BsCheckCircle } from 'react-icons/bs'; 

function FormApiCall() {
  const [selectedFilePath, setSelectedFilePath] = useState(null);
  const [response, setResponse] = useState({});
  const [conversionStatus, setConversionStatus] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFilePath(event.target.files[0]);
    setConversionStatus(false);
  };
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    if (selectedFilePath) {
      try {
        const requestData = `{"file_path": "${selectedFilePath.path}"}`;
        console.log(requestData);
        const response = await fetch('http://localhost:8080/convert', {
          method: 'POST',
          body: requestData,
          headers: {
            'Content-Type': 'application/json',
            mode: 'no-cors',
          },
        });
  
        const result = await response.json();
        setResponse(result);
        setConversionStatus(true);
      } catch (error) {
        console.error('Error:', error);
      }
    } else {
      alert('Please choose a file.');
    }
  };
  
  return (
    <Form onSubmit={handleSubmit} className="form-api-call">
      <Form.Group controlId="formFileLg" className="mb-3">
        <Form.Label className="form-label">Bitte .Docx-File eingeben:</Form.Label>
        <Form.Control
          type="file"
          accept=".docx"
          size="lg"
          onChange={handleFileChange}
          className="form-control"
        />
      </Form.Group>
      <Button variant="primary" type="submit" className="submit-button">
        Umwandeln!
      </Button>
      {conversionStatus && response && 
        <>
          <Alert variant="success" className="success-message"><BsCheckCircle className="check-icon" /> Conversion Successful!</Alert>
          <div className="response">
            <h2>Response</h2>
            <p><strong>Message:</strong> {response.message}</p>
            <p><strong>Changes:</strong> {response.changes}</p>
            <p><strong>New file path:</strong> {response.new_file_path}</p>
            {response.error && <p><strong>Error:</strong> {response.error}</p>}
          </div>
        </>
      }
    </Form>
  );
}

export default FormApiCall;
