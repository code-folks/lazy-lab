import { unref } from 'vue';
import { createSharedComposable } from '@vueuse/core';

import { initializeApp, FirebaseApp } from 'firebase/app';
import { getAuth, connectAuthEmulator, Auth } from 'firebase/auth';

import { firebaseConfig, emulatorsConfig } from './config';
import { useDev } from '../composables';


interface useFirebaseComposable {
    app: FirebaseApp,
    auth: Auth,
}


function $useFirebase(): useFirebaseComposable {
    const { isDev } = useDev();
    const firebaseApp: FirebaseApp = initializeApp(firebaseConfig);
    const firebaseAuth: Auth = getAuth(firebaseApp);

    if(unref(isDev)) {
        connectAuthEmulator(firebaseAuth, emulatorsConfig.auth.url);
    } 
    console.log(emulatorsConfig);
    return {
        app: firebaseApp,
        auth: firebaseAuth,
    };
}


const useFirebase = createSharedComposable($useFirebase);

export {
    useFirebase,
}