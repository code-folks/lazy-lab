import { defineStore} from 'pinia' ;
import { useAuth as $useAuth } from '@vueuse/firebase';

import { User, UserCredential, signInWithEmailAndPassword } from 'firebase/auth';

import { useFirebase } from '../firebase/useFirebase';
import { Ref, ref } from 'vue';


export const useAuth = defineStore('auth', () => {
  const { auth } = useFirebase();
  const { isAuthenticated, user } = $useAuth(auth);

  const isLoading: Ref<boolean> = ref(false);

  function signIn(username:string, password: string) {
    isLoading.value = true;
    return signInWithEmailAndPassword(auth, username, password).finally(
      () => { 
        isLoading.value = false;
      }
    )
  }

  return {
    isAuthenticated,
    isLoading,
    user,
    signIn,
  }
});
