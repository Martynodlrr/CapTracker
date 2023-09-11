import { useParams, useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import React, { useEffect, useState } from 'react';

import greetings from './greetings';

import './index.css';

function Profile() {
  const { userId } = useParams();
  const history = useHistory();
  // const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [previewSrc, setPreviewSrc] = useState(user?.pfp || null);
  const [firstName, setFirstName] = useState(user.firstName);
  const [lastName, setLastName] = useState(user.lastName);
  const [userName, setUserName] = useState(user.userName);
  const [pfp, setPfp] = useState(user?.pfp || null);
  const [disabled, setDisabled] = useState(false);
  const [email, setEmail] = useState(user.email);
  const [greeting, setGreeting] = useState("");

  useEffect(() => {
    setGreeting(greetings[Math.floor(Math.random() * greetings.length)]);
  }, []);

  useEffect(() => {
    if (userId !== user.id) {
      history.push(`/users/${user.id}`);
    }
  }, [userId, user.id, history]);

  useEffect(() => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // A basic regex to validate email format
    setDisabled(
      firstName.length < 2 ||
      firstName.length > 25 ||
      lastName.length < 2 ||
      lastName.length > 50 ||
      userName.length < 4 ||
      userName.length > 40 ||
      email.length > 75 ||
      !emailRegex.test(email)
      // Add a password length check if you have a password state variable
      // || password.length < 6
    );
  }, [firstName, lastName, userName, email /* , password */]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const updatedUser = {
      firstName,
      lastName,
      userName,
      email,
      pfp: pfp === "https://i.pinimg.com/originals/09/f0/84/09f084cd8a8093ea5738a3ab75c210df.png" ? false : pfp,
      userId: user.id
    }

    console.log(updatedUser)
    // dispatch(sessionActions.update(updatedUser, user.id))
    // .catch((e) => {
    //   console.error("Error updating user: ", e);
    // });
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setPfp(file);
      const src = URL.createObjectURL(file);
      if (previewSrc) URL.revokeObjectURL(previewSrc);
      setPreviewSrc(src);
    } else {
      setPreviewSrc(user?.pfp || null);
    }
  };

  return (
    <>
      <h1>{greeting}</h1>
      <form onSubmit={handleSubmit} encType="multipart/form-data" id='profile-form'>
        <div className="form-field">
          <label htmlFor="firstName" className='profile-label'>First Name</label>
          <input
            id="firstName"
            className='profile-input'
            type="text"
            onChange={(e) => setFirstName(e.target.value)}
            value={firstName}
            placeholder="First Name"
            required={true}
          />
        </div>

        <div className="form-field">
          <label htmlFor="lastName" className='profile-label'>Last Name</label>
          <input
            id="lastName"
            className='profile-input'
            type="text"
            onChange={(e) => setLastName(e.target.value)}
            value={lastName}
            placeholder="Last Name"
            required={true}
          />
        </div>

        <div className="form-field">
          <label htmlFor="userName" className='profile-label'>Username</label>
          <input
            id="userName"
            className='profile-input'
            type="text"
            onChange={(e) => setUserName(e.target.value)}
            value={userName}
            placeholder="Username"
            required={true}
          />
        </div>

        <div className="form-field">
          <label htmlFor="email" className='profile-label'>Email</label>
          <input
            id="email"
            className='profile-input'
            type="email"
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            placeholder="Email"
            required={true}
          />
        </div>

        <div className='file-input-container'>
          <span className="pfp-render">
            <img src={previewSrc} alt={`${firstName} ${lastName} Profile Preview`} id='profile-picture' />
          </span>
          <button type="button" className="file-select-button" onClick={() => document.getElementById('pfp-input').click()}>Select File</button>
          <input
            id="pfp-input"
            className='profile-input-hidden'
            type="file"
            accept="image/*"
            onChange={handleFileChange}
          />
        </div>

        <button type="submit" className="form-submit" disabled={disabled}>Update Profile</button>
      </form>
    </>
  );
}

export default Profile;
