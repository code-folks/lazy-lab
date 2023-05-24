import { FirebaseOptions } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

interface AuthEmulatorConfig {
    url: string
}

interface StorageEmulatorConfig {
    host: string,
    port: number
}


interface EmulatorsOptions {
    auth: AuthEmulatorConfig,
    storage?: StorageEmulatorConfig
}

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
export const firebaseConfig: FirebaseOptions = {
    apiKey: "AIzaSyDF6o_70iQwg3KCcVorGexjW92eZVcjcC0",
    authDomain: "lazy-lab-b2746.firebaseapp.com",
    projectId: "lazy-lab-b2746",
    storageBucket: "lazy-lab-b2746.appspot.com",
    messagingSenderId: "665579171003",
    appId: "1:665579171003:web:cbbfb6f9f5996226fe0d9e",
    measurementId: "G-61JGDRSRHD"
};

export const emulatorsConfig: EmulatorsOptions = {
    auth: {
        url: "http://127.0.0.1:9081" 
    },
    storage: {
        host: "http://localhost",
        port: 9082
    }
}

