import { defineStore } from 'pinia';

import { inMemoryPersistence, signInWithEmailAndPassword, User } from 'firebase/auth';

import { useFirebase } from '../firebase/useFirebase';
import { Ref, ref, computed } from 'vue';


export const useAuth = defineStore('auth', () => {
  const { auth } = useFirebase();
  const user: Ref<User | null> = ref(auth.currentUser);
  const isAuthenticated = computed(() => !!user);

  auth.onAuthStateChanged((userState: User | null) => user.value = userState);

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
