import React from 'react'
import Image from 'next/image'
import styles from './page.module.css'

function jsonToTable(jsonData) {
  let tableHtml = '<table style="border-collapse: collapse; border: 1px solid black; text-align: left;">';
  if (jsonData && jsonData.length > 0) {
    tableHtml += '<tr>';
    Object.keys(jsonData[0]).forEach(key => {
      tableHtml += `<th style="border: 1px solid black; padding: 8px;">${key}</th>`;
    });
    tableHtml += '</tr>';
    jsonData.forEach(item => {
      tableHtml += '<tr>';
      Object.values(item).forEach(value => {
        tableHtml += `<td style="border: 1px solid black; padding: 8px;">${value}</td>`;
      });
      tableHtml += '</tr>';
    });
  } else {
    tableHtml += '<tr><td colspan="4">No data available</td></tr>';
  }
  tableHtml += '</table>';
  return tableHtml;
}

const searchADocumentByID = () => {
  return (
    <>
      <div className={styles.loginPageContainer}>
        <div className={styles.imageContainer}>
          <Image className={styles.image} src={'/gifs/search_admin.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
        </div>
        <form className={styles.formContainer} onSubmit={
              async (event) => {
                event.preventDefault()
                const readerid = event.target.readerid.value
                const dynamicapi = 'http://localhost:8000/cityLibrary/reader/getReservedDocument/' + readerid
                const response = await fetch(dynamicapi)
                const data = await response.json()
                var resultOverlay = document.getElementById('overlayResult')
                resultOverlay.style.display = 'flex'
                let content = "<div style='height: 100%; display: flex; flex-direction: column; margin: 1rem 0rem; padding: 0rem 4rem;'>";
                content += "<h1 style='font-size: 2rem'>Your Reserved Documents</h1>"
                if (data.status == "success" && data.hasOwnProperty('descriptive_error') == false){
                  content += jsonToTable(data.query_result); 
                }
                else if (data.hasOwnProperty('descriptive_error') == true) {
                  content += "<p>" + data.descriptive_error + "</p>";
                }
                else 
                {
                  content += "<p>You have not reserved any document.</p>";
                }
                content += "<button style='width: 20%; margin: 1rem 0rem; border-radius: 5rem; background-color: rgb(243, 181, 106); color: black; boder: 2px solid black; font-size: 1.2rem;' onClick=\"window.location.href='/ReaderDashboard'\">Close</button>";
                content += "</div>";
                resultOverlay.innerHTML = content;
              }
          }>
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Reader ID: </label>
            <input className={styles.input} type="text" id="readerid" name="username" required/>
          </div>
          
          <div className={styles.buttonPlaceHolder}>
            <button className={styles.submitButton} type="submit">My Reserved Documents</button>
          </div>
        </form>
      </div>

      <div id="overlayResult" className={styles.overlayResult}>
      </div>
    </>
  )
}

export default searchADocumentByID