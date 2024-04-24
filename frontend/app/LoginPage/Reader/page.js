import React from 'react'
import styles from './page.module.css'
import Image from 'next/image'

const readerloginpage = () => {
  return (
    <div className={styles.loginPageContainer}>
      <h2 className={styles.loginText}>Reader Login</h2>
      <div className={styles.imageContainer}>
        <Image className={styles.image} src={'/gifs/reader_library_login.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
      </div>
      <form className={styles.formContainer}>
        <div className={styles.placeHolder}>
          <label className={styles.label} htmlFor="username">Reader ID: </label>
          <input className={styles.input} type="text" id="username" name="username" required/>
        </div>

        <div className={styles.buttonPlaceHolder}>
          <button className={styles.submitButton} type="submit">Login</button>
        </div>
      </form>
    </div>
  )
}

export default readerloginpage