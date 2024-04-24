import React from 'react'
import Image from 'next/image'
import styles from './page.module.css'

function jsonToTable(jsonData) {
  let tableHtml = '<table style="border-collapse: collapse; border: 1px solid black; text-align: left;">';
  tableHtml += '<tr>';
  for (let key in jsonData) {
    if (jsonData.hasOwnProperty(key)) {
      tableHtml += `<th style="border: 1px solid black; padding: 8px; text-align: left;">${key}</th>`;
    }
  }
  tableHtml += '</tr>';
  tableHtml += '<tr>';
  for (let key in jsonData) {
    if (jsonData.hasOwnProperty(key)) {
      tableHtml += `<td style="border: 1px solid black; padding: 8px; text-align: left;">${jsonData[key]}</td>`;
    }
  }
  tableHtml += '</tr>';
  tableHtml += '</table>';
  return tableHtml;
}


const addAReader = () => {
  return (
    <>
      <div className={styles.loginPageContainer}>
        <div className={styles.imageContainer}>
          <Image className={styles.image} src={'/gifs/reader_admin.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
        </div>
        <form className={styles.formContainer} onSubmit={
              async (event) => {
                event.preventDefault()
                const readername = event.target.readername.value
                const profession = event.target.profession.value
                const address = event.target.address.value
                const contact = event.target.contact.value
                const dynamicapi = 'http://localhost:8000/cityLibrary/admin/addReader/' + readername + '/' + profession + '/' + address + '/' + contact
                const response = await fetch(dynamicapi)
                const data = await response.json()
                var resultOverlay = document.getElementById('overlayResult')
                resultOverlay.style.display = 'flex'
                let content = "<div style='display: flex; flex-direction: column; margin-top: 10px; padding: 0rem 5rem;'>";
                content += "<h1 style='font-size: 2rem'>Adding A Reader</h1>"
                if (data.status == "success" && data.hasOwnProperty('error') == false){
                  content += "<p>Added A New Reader with following details: </p>";
                  content += jsonToTable(data.new_reader_details); // Assuming jsonToTable function returns a table HTML string
                  content += "<p>Make sure, the reader is provided with his/her Reader ID, as it will be later required for all further processes with the library.</p>"
                }
                else if (data.error) {
                  content += "<p>" + data.descriptive_error + "</p>";
                }
                else 
                {
                  content += "<p>Failed to add the reader data. Please check the data that you have entered.</p>";
                }
                content += "<button style='width: 20%; border-radius: 5rem; background-color: rgb(243, 181, 106); color: black; boder: 2px solid black; font-size: 1.2rem;' onClick=\"window.location.href='/AdminDashboard'\">Close</button>";
                content += "</div>";
                resultOverlay.innerHTML = content;
              }
          }>
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Reader Name: </label>
            <input className={styles.input} type="text" id="readername" name="username" required/>
          </div>

          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Profession: </label>
            <input className={styles.input} type="text" id="profession" name="username" required/>
          </div>
          
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Address: </label>
            <input className={styles.input} type="text" id="address" name="username" required/>
          </div>

          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Contact Information: </label>
            <input className={styles.input} type="text" id="contact" name="username" required/>
          </div>

          <div className={styles.buttonPlaceHolder}>
            <button className={styles.submitButton} type="submit">Add Reader</button>
          </div>
        </form>
      </div>

      <div id="overlayResult" className={styles.overlayResult}>
      </div>
    </>
  )
}

export default addAReader