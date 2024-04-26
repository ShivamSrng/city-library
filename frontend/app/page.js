'use client';
import { useEffect } from 'react';
import styles from "./page.module.css";
import Admin from './LoginPage/Admin/page'
import Reader from './LoginPage/Reader/page'


export default function Home() {
  useEffect( () => {
    (
      async () => {
          const LocomotiveScroll = (await import('locomotive-scroll')).default
          const locomotiveScroll = new LocomotiveScroll();
      }
    )()
  }, [])


  return (
    <main className={styles.main}>
      <h1 className={styles.title}>CITY LIBRARY MANAGEMENT SYSTEM</h1>
      <div className={styles.loginContainer}>
        <div className={styles.formContainer}>
          <Admin />
          <Reader />
        </div>
      </div>
    </main>
  );
}
