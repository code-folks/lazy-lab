import { defineStore } from 'pinia';
import { useAuth as $useAuth } from '@vueuse/firebase';

import { inMemoryPersistence, signInWithEmailAndPassword } from 'firebase/auth';

import { useFirebase } from '../firebase/useFirebase';
import { Ref, ref } from 'vue';


export const useAuth = defineStore('auth', () => {
  const { auth } = useFirebase();
  const { isAuthenticated, user } = $useAuth(auth);

  const isLoading: Ref<boolean> = ref(false);

  function signIn(username: string, password: string, remember: boolean = true) {
    isLoading.value = true;
    let signInPromise = signInWithEmailAndPassword(auth, username, password);
    if (!remember) {
      signInPromise = auth.setPersistence(inMemoryPersistence).then(
        () => signInWithEmailAndPassword(auth, username, password)
      )
    }
    return signInPromise.finally(
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
