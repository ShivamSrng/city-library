import React from 'react'
import Image from 'next/image'
import styles from './page.module.css'

const addADocument = () => {
  return (
    <>
      <div className={styles.loginPageContainer}>
        <div className={styles.imageContainer}>
          <Image className={styles.image} src={'/gifs/document_admin.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
        </div>
        <form className={styles.formContainer} onSubmit={
              async (event) => {
                event.preventDefault()
                const documentid = event.target.documentid.value
                const branchid = event.target.branchid.value
                const dynamicapi = 'http://localhost:8000/cityLibrary/admin/addDocumentCopy/' + documentid + '/' + branchid
                const response = await fetch(dynamicapi)
                const data = await response.json()
                var resultOverlay = document.getElementById('overlayResult')
                resultOverlay.style.display = 'flex'
                if (data.result) {
                  resultOverlay.innerHTML = "Copy Added Successfully, with details as: " + JSON.stringify(data.new_copy_details) + ".<br>"
                  resultOverlay.innerHTML += "<button onClick={function f() {window.location.href='/AdminDashboard' resultOverlay.style.display = 'none'}}>Close</button>"
                } else {
                  resultOverlay.innerHTML = "Failed to add copy. Please check the document ID and branch ID."
                  resultOverlay.innerHTML += "<button onClick={function f() {window.location.href='/AdminDashboard' resultOverlay.style.display = 'none'}}>Close</button>"
                }
                // window.location.href = '/AdminDashboard'
              }
          }>
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Document ID: </label>
            <input className={styles.input} type="text" id="documentid" name="username" required/>
          </div>
          
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Branch ID: </label>
            <input className={styles.input} type="text" id="branchid" name="username" required/>
          </div>

          <div className={styles.buttonPlaceHolder}>
            <button className={styles.submitButton} type="submit">Add Copy</button>
          </div>
        </form>
      </div>

      <div id="overlayResult" className={styles.overlayResult}>
      </div>
    </>
  )
}

export default addADocument