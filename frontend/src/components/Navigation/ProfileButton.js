import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import React, { useState, useEffect, useRef } from "react";
import { useHistory } from 'react-router-dom';
import { useDispatch } from "react-redux";

import OpenModalButton from "../OpenModalButton";
import SignupFormModal from "../SignupFormModal";
import LoginFormModal from "../LoginFormModal";
import { logout } from "../../store/session";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  const handleProfileRedirect = () => {
    history.push(`/users/${user.id}`);
  };

  const handleCapstoneRedirect = () => {
    history.push(`/capstone/edit`);
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu}>
        <FontAwesomeIcon icon={faBars} />
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <li><img src={user.pfp} alt="User's Profile" id="pfp" /></li>
            <li>{user.username}</li>
            <li><button onClick={handleProfileRedirect}>Profile</button></li>
            <li><button onClick={handleCapstoneRedirect}>Capstone</button></li>
            <nav>
              <button onClick={handleLogout}>Log Out</button>
            </nav>
          </>
        ) : (
          <>
            <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />

            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            />
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
