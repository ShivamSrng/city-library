'use client';
import React, { useState } from 'react'
import styles from './page.module.css'
import SearchADocumentByID from '../ReaderFunctions/SearchDocumentByID/page';
import SearchADocumentByTitle from '../ReaderFunctions/SearchDocumentByTitle/page';
import SearchADocumentByPublisherName from '../ReaderFunctions/SearchDocumentByPublisherName/page';
import RetrieveBranchInformation from '../AdminFunctions/RetrieveBranchInformation/page'
import MostFrequentBorrowerOfBranch from '../AdminFunctions/MostFrequentBorrowersOfBranch/page'
import MostFrequentBorrowerOfLibrary from '../AdminFunctions/MostFrequentBorrowerOfLibrary/page'
import MostBorrowedBooksInBranch from '../AdminFunctions/MostBorrowedBooksInBranch/page'
import ComputeFine from '../ReaderFunctions/ComputeFine/page'
import GetReservedDocuments from '../ReaderFunctions/GetReservedDocuments/page'
import SearchADocumentByPublisherNameConstrained from '../ReaderFunctions/SearchDocumentByPublisherNameConstrained/page'


const RenderFormTitle = ({index}) => {
  switch(index) {
    case 0:
      return "Search a Document by ID"
    case 1:
      return "Search a Document by Title"
    case 2:
      return "Search a Document by Publisher Name"
    case 3:
      return "Document Checkout"
    case 4:
      return "Document Return"
    case 5:
      return "Document Reserve"
    case 6:
      return "Compute fine for a Reader"
    case 7:
      return "List of Documents Reserved by a Reader and their Status"
    case 8:
      return "Document ID and Document Titles of Documents Published by a Publisher"
  }
}

const RenderFormComponent = ({index}) => {
  switch(index) {
    case 0:
      return <SearchADocumentByID />
    case 1:
      return <SearchADocumentByTitle />
    case 2:
      return <SearchADocumentByPublisherName />
    case 3:
      return <RetrieveBranchInformation />
    case 4:
      return <MostFrequentBorrowerOfBranch />
    case 5:
      return <MostFrequentBorrowerOfLibrary />
    case 6:
      return <ComputeFine />
    case 7:
      return <GetReservedDocuments />
    case 8:
      return <SearchADocumentByPublisherNameConstrained />
  }
}

const adminDashboard = () => {
  const[formTitle, setFormTitle] = useState("Search a document by ID.")
  const[isSelected, setIsSelected] = useState(0)
  return (
    <>
      <div className={styles.adminDashboardContainer}>
        <div className={styles.dataContainer}>
          <div className={styles.splitContainer}>
            <div className={styles.titleContainer}>
              <h1>Reader Panel</h1>
            </div>
            <div className={styles.adminMenu}>
              <div><h2>Reader's Functions Menu</h2></div>
              <ol>
                <li onClick={
                  async () => {
                    setFormTitle("Search a document by ID")
                    setIsSelected(0)
                  }
                }>Search a document by ID.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Search a document by Title")
                    setIsSelected(1)
                  }
                }>Search a document by Title.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Search a document by Publisher Name")
                    setIsSelected(2)
                  }
                }>Search a document by Publisher Name.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Document checkout")
                    setIsSelected(3)
                  }
                }>Document checkout.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Document return")
                    setIsSelected(4)
                  }
                }>Document return.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Document reserve")
                    setIsSelected(5)
                  }
                }>Document reserve.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Compute fine for a document copy borrowed by a reader based on the current date")
                    setIsSelected(6)
                  }
                }>Compute fine for a document copy borrowed by a reader based on the current date.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Print the list of documents reserved by a reader and their status")
                    setIsSelected(7)
                  }
                }>Print the list of documents reserved by a reader and their status.</li>
                <li onClick={
                  async () => {
                    setFormTitle("Print the document id and document titles of documents published by a publisher")
                    setIsSelected(8)
                  }
                }>Print the document id and document titles of documents published by a publisher.</li>
              </ol>
              <button className={styles.submitButton} onClick={() => window.location.href = '/'}>Logout</button>
            </div>
          </div>

          <div className={styles.respectiveFormContainer}>
            <div className={styles.formTitleContainer}>
              <h2>{RenderFormTitle({index: isSelected})}</h2>
            </div>
            <div className={styles.formContainer}>
              {RenderFormComponent({index: isSelected})}
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default adminDashboard