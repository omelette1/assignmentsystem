import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function MyButton() {
    return (
      <button onClick={() => alert('Button clicked!')}>
        Click me to kill yourself!
      </button>
    );
  }
export default MyButton;