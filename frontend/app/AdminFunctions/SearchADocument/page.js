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

const searchADocument = () => {
  return (
    <>
      <div className={styles.loginPageContainer}>
        <div className={styles.imageContainer}>
          <Image className={styles.image} src={'/gifs/search_admin.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
        </div>
        <form className={styles.formContainer} onSubmit={
              async (event) => {
                event.preventDefault()
                const documentid = event.target.documentid.value
                const copyid = event.target.copyid.value
                const branchid = event.target.branchid.value
                const dynamicapi = 'http://localhost:8000/cityLibrary/admin/searchDocumentCopy/' + documentid + '/' + copyid + '/' + branchid
                const response = await fetch(dynamicapi)
                const data = await response.json()
                var resultOverlay = document.getElementById('overlayResult')
                resultOverlay.style.display = 'flex'
                let content = "<div style='display: flex; flex-direction: column; margin-top: 10px; padding: 0rem 5rem;'>";
                content += "<h1 style='font-size: 2rem'>Searching A Document</h1>"
                if (data.status == "success" && data.hasOwnProperty('descriptive_error') == false){
                  content += "<p>A Document Copy found with mentioned details: </p>";
                  content += jsonToTable(data.query_result); // Assuming jsonToTable function returns a table HTML string
                  content += "<p>Using the position of the copy, you can locate the document's copy in the library. For example, if the position is '001A03', it means that the copy of that document is in the third shelve of bookcase A03</p>"
                }
                else if (data.descriptive_error) {
                  content += "<p>" + data.descriptive_error + "</p>";
                }
                else 
                {
                  content += "<p>Copy failed to be added. Please check the data that you have entered.</p>";
                }
                content += "<button style='width: 20%; border-radius: 5rem; background-color: rgb(243, 181, 106); color: black; boder: 2px solid black; font-size: 1.2rem;' onClick=\"window.location.href='/AdminDashboard'\">Close</button>";
                content += "</div>";
                resultOverlay.innerHTML = content;
              }
          }>
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Document ID: </label>
            <input className={styles.input} type="text" id="documentid" name="username" required/>
          </div>

          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Copy ID: </label>
            <input className={styles.input} type="text" id="copyid" name="username" required/>
          </div>
          
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Branch ID: </label>
            <input className={styles.input} type="text" id="branchid" name="username" required/>
          </div>

          <div className={styles.buttonPlaceHolder}>
            <button className={styles.submitButton} type="submit">Search Copy</button>
          </div>
        </form>
      </div>

      <div id="overlayResult" className={styles.overlayResult}>
      </div>
    </>
  )
}

export default searchADocument