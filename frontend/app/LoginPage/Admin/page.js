import React from 'react';
import styles from './page.module.css';
import Image from 'next/image';


function adminloginPage() {
  return (
    <div className={styles.loginPageContainer}>
      <h2 className={styles.loginText}>Admin Login</h2>
      <div className={styles.imageContainer}>
        <Image className={styles.image} src={'/gifs/admin_library_login.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
      </div>
      <form className={styles.formContainer} onSubmit={
            async (event) => {
              event.preventDefault()
              const username = event.target.username.value
              const password = event.target.password.value
              const dynamicapi = 'http://localhost:8000/cityLibrary/admin/validation/' + username + '/' + password
              const response = await fetch(dynamicapi)
              const data = await response.json()
              if (data.result) {
                alert('Login Successful')
                window.location.href = '/AdminDashboard'
              } else {
                alert('Login Failed')
              }
            }
        }>
        <div className={styles.placeHolder}>
          <label className={styles.label} htmlFor="username">Username: </label>
          <input className={styles.input} type="text" id="username" name="username" required/>
        </div>
        
        <div className={styles.placeHolder}>
          <label className={styles.label} htmlFor="password">Password: </label>
          <input className={styles.input} type="password" id="password" name="password" required/>
        </div>

        <div className={styles.buttonPlaceHolder}>
          <button className={styles.submitButton} type="submit">Login</button>
        </div>
      </form>
    </div>
  )
}

export default adminloginPage