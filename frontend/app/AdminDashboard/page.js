'use client';
import React, { useState } from 'react'
import styles from './page.module.css'
import AddADocument from '../AdminFunctions/AddADocument/page'
import SearchADocument from '../AdminFunctions/SearchADocument/page'
import AddAReader from '../AdminFunctions/AddAReader/page'
import RetrieveBranchInformation from '../AdminFunctions/RetrieveBranchInformation/page'
import MostFrequentBorrowerOfBranch from '../AdminFunctions/MostFrequentBorrowersOfBranch/page'
import MostFrequentBorrowerOfLibrary from '../AdminFunctions/MostFrequentBorrowerOfLibrary/page'
import MostBorrowedBooksInBranch from '../AdminFunctions/MostBorrowedBooksInBranch/page'
import MostBorrowedBooksInLibrary from '../AdminFunctions/MostBorrowedBooksOfLibrary/page'
import MostPopularBooksInLibraryYear from '../AdminFunctions/MostPopularBookInLibraryYear/page'
import ComputeFine from '../AdminFunctions/ComputeFine/page'


const RenderFormTitle = ({index}) => {
  switch(index) {
    case 0:
      return "Add a Document"
    case 1:
      return "Search a Document"
    case 2:
      return "Add a Reader"
    case 3:
      return "Print Branch Information"
    case 4:
      return "Get top N most frequent borrowers in branch I"
    case 5:
      return "Get top N most frequent borrowers in the library"
    case 6:
      return "Get N most borrowed books in branch I"
    case 7:
      return "Get N most borrowed books in the library"
    case 8:
      return "Get 10 most popular books of a year"
    case 9:
      return "Get average fine paid by borrowers to a branch"
  }
}

const RenderFormComponent = ({index, username}) => {
  switch(index) {
    case 0:
      return <AddADocument username={username}/>
    case 1:
      return <SearchADocument username={username}/>
    case 2:
      return <AddAReader username={username} />
    case 3:
      return <RetrieveBranchInformation username={username}/>
    case 4:
      return <MostFrequentBorrowerOfBranch username={username}/>
    case 5:
      return <MostFrequentBorrowerOfLibrary username={username}/>
    case 6:
      return <MostBorrowedBooksInBranch username={username}/>
    case 7:
      return <MostBorrowedBooksInLibrary username={username}/>
    case 8:
      return <MostPopularBooksInLibraryYear username={username}/>
    case 9:
      return <ComputeFine username={username}/>
  }
}

const adminDashboard = () => {
  const[formTitle, setFormTitle] = useState("Add A Document Copy")
  const[isSelected, setIsSelected] = useState(0)
  const queryParameters = new URLSearchParams(window.location.search)
  var username = queryParameters.get('username')
  var correctedusername = username.charAt(0).toUpperCase() + username.slice(1)
  return (
    <>
      <div className={styles.adminDashboardContainer}>
        <div className={styles.dataContainer}>
          <div className={styles.splitContainer}>
            <div className={styles.titleContainer}>
              <h1>Hello, <span className={styles.titleUsername}>{correctedusername}</span> !</h1>
            </div>
            <div className={styles.adminMenu}>
              <div><h2>Administrative Functions Menu</h2></div>
              <ol>
                <li onClick={
                  async () => {
                    setFormTitle("Add A Document Copy")
                    setIsSelected(0)
                  }
                }>Add a Document Copy.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Search A Document")
                    setIsSelected(1)
                  }
                }>Search document copy and check its status.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Add A Reader")
                    setIsSelected(2)
                  }
                }>Add new reader.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Print Branch Information")
                    setIsSelected(3)
                  }
                }>Print branch information (name and location).</li>
                <li onClick={
                  async () => {
                    setFormTitle("Get top N most frequent borrowers in branch I")
                    setIsSelected(4)
                  }
                }>Get number N and branch number I as input and print the top N most frequent borrowers (Rid and name) in branch I and the number of books each has borrowed.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Get top N most frequent borrowers in Library")
                    setIsSelected(5)
                  }
                }>Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Get N most borrowed books in branch I")
                    setIsSelected(6)
                  }
                }>Get number N and branch number I as input and print the N most borrowed books in branch I.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Get N most borrowed books in the library")
                    setIsSelected(7)
                  }
                }>Get number N as input and print the N most borrowed books in the library.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Get 10 most popular books of a year")
                    setIsSelected(8)
                  }
                }>Get a year as input and print the 10 most popular books of that year in the library.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Get average fine paid by borrowers to a branch")
                    setIsSelected(9)
                  }
                }>Get a start date S and an end date E as input and print, for each branch, the branch Id and name and the average fine paid by the borrowers for documents borrowed from this branch during the corresponding period of time.</li>
              </ol>
              <button className={styles.submitButton} onClick={() => window.location.href = '/'}>Logout</button>
            </div>
          </div>

          <div className={styles.respectiveFormContainer}>
            <div className={styles.formTitleContainer}>
              <h2>{RenderFormTitle({index: isSelected})}</h2>
            </div>
            <div className={styles.formContainer}>
              {RenderFormComponent({index: isSelected, username: username})}
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default adminDashboard