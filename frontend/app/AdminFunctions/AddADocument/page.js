import React from 'react'
import Image from 'next/image'
import styles from './page.module.css'

function jsonToTable(jsonData) {
  let tableHtml = '<div style="padding: 1.5rem 0rem;"><table style="border-collapse: collapse; border: 1px solid #ddd;">';
  tableHtml += '<tr>';
  for (let key in jsonData) {
    if (jsonData.hasOwnProperty(key)) {
      tableHtml += `<th style="border: 1px solid black; padding: 1rem 1rem; text-align: left;">${key}</th>`;
    }
  }
  tableHtml += '</tr>';
  tableHtml += '<tr>';
  for (let key in jsonData) {
    if (jsonData.hasOwnProperty(key)) {
      tableHtml += `<td style="border: 1px solid black; padding: 1rem 1rem; text-align: left;">${jsonData[key]}</td>`;
    }
  }
  tableHtml += '</tr>';
  tableHtml += '</table></div>';
  return tableHtml;
}


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
                if (data.status == "success") {
                  let content = "<div style='display: flex; flex-direction: column; margin-top: 10px;'>";
                  content += "<p>Copy Added Successfully, with details as: </p>";
                  content += jsonToTable(data.new_copy_details); // Assuming jsonToTable function returns a table HTML string
                  content += "<button style='width: 20%; border-radius: 5rem; background-color: rgb(243, 181, 106); color: black; boder: 2px solid black; font-size: 1.2rem;' onClick=\"window.location.href='/AdminDashboard'\">Close</button>";
                  content += "</div>";
                  resultOverlay.innerHTML = content;
                } else {
                  let content = "<div style='display: flex; flex-direction: column;'>";
                  content += "<p>Copy failed to be added. Please check the data that you have entered.</p>";
                  content += "<button style='width: 20%; border-radius: 5rem; background-color: rgb(243, 181, 106); color: black; boder: 2px solid black; font-size: 1.2rem;' onClick=\"window.location.href='/AdminDashboard'\">Close</button>";
                  content += "</div>";
                  resultOverlay.innerHTML = content;
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