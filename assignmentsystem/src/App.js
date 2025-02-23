import React from 'react';
import logo from './logo.svg';
import './App.css';
import AssignmentHome from './AssigmentHome';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/assignment" />} />
        <Route path='/assignment' element={<AssignmentHome />} />

      </Routes>
    </Router>
  );
}

export default App;
