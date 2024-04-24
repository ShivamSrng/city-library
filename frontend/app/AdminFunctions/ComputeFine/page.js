import React from 'react'
import Image from 'next/image'
import styles from './page.module.css'

function jsonToTable(jsonData) {
  let tableHtml = '<table style="border-collapse: collapse; border: 1px solid black; text-align: left;">';
  if (jsonData && jsonData.length > 0) {
    tableHtml += '<tr>';
    Object.keys(jsonData[0]).forEach(key => {
      tableHtml += `<th style="border: 1px solid black; padding: 8px; background-color: rgb(243, 181, 106);">${key}</th>`;
    });
    tableHtml += '</tr>';
    var cnt = 0;
    jsonData.forEach(item => {
      if (cnt % 2 == 0)
        tableHtml += "<tr style='background-color: rgb(255, 211, 158);'>";
      else
        tableHtml += "<tr>";
      Object.values(item).forEach(value => {
        tableHtml += `<td style="border: 1px solid black; padding: 8px;">${value}</td>`;
      });
      cnt++;
      tableHtml += '</tr>';
    });
  } else {
    tableHtml += '<tr><td colspan="4">No data available</td></tr>';
  }
  tableHtml += '</table>';
  return tableHtml;
}


const computeFine = () => {
  return (
    <>
      <div className={styles.loginPageContainer}>
        <div className={styles.imageContainer}>
          <Image className={styles.image} src={'/gifs/borrowed_book_branch_admin.gif'} alt="Admin" layout={'responsive'} width={50} height={50} />
        </div>
        <form className={styles.formContainer} onSubmit={
              async (event) => {
                event.preventDefault()
                const stime = event.target.stime.value
                const etime = event.target.etime.value
                const branchname = event.target.branchname.value
                const dynamicapi = 'http://localhost:8000/cityLibrary/admin/computeFineCollectedByBranch/' +  stime + '/' + etime + '/' + branchname
                const response = await fetch(dynamicapi)
                const data = await response.json()
                var resultOverlay = document.getElementById('overlayResult')
                resultOverlay.style.display = 'flex'
                let content = "<div style='display: flex; flex-direction: column; margin-top: 10px; padding: 0rem 5rem;'>";
                content += "<h1 style='font-size: 2rem'>Compute Fine Collected By Branch: '" + branchname +"'</h1>"
                if (data.status == "success" && data.hasOwnProperty('descriptive_error') == false){
                  content += jsonToTable(data.query_result);
                }
                else if (data.descriptive_error) {
                  content += "<p>" + data.descriptive_error + "</p>";
                }
                else 
                {
                  content += "<p>Failed to fetch the collected fine for the provided branch.</p>";
                }
                content += "<button style='width: 20%; margin-top: 1rem; border-radius: 5rem; background-color: rgb(243, 181, 106); color: black; boder: 2px solid black; font-size: 1.2rem;' onClick=\"window.location.href='/AdminDashboard'\">Close</button>";
                content += "</div>";
                resultOverlay.innerHTML = content;
              }
          }>
          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Start Date and Time (YYYY-MM-DD HH:MM:SS): </label>
            <input className={styles.input} type="text" id="stime" name="username" required/>
          </div>

          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">End Date and Time (YYYY-MM-DD HH:MM:SS): </label>
            <input className={styles.input} type="text" id="etime" name="username" required/>
          </div>

          <div className={styles.placeHolder}>
            <label className={styles.label} htmlFor="username">Branch ID: </label>
            <input className={styles.input} type="text" id="branchname" name="username" required/>
          </div>

          <div className={styles.buttonPlaceHolder}>
            <button className={styles.submitButton} type="submit">Compute</button>
          </div>
        </form>
      </div>

      <div id="overlayResult" className={styles.overlayResult}>
      </div>
    </>
  )
}

export default computeFine