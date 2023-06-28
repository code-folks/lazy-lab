import { defineStore } from 'pinia';


import { Ref, ref, computed } from 'vue';


export const useAuth = defineStore('auth', () => {
  // const { auth } = useFirebase();
  const user: Ref<null> = ref(null);
  const isAuthenticated = computed(() => !!user);


  const isLoading: Ref<boolean> = ref(false);

  function signIn(username: string, password: string, remember: boolean = true) {
    isLoading.value = true;
    let signInPromise = new Promise(() => {}); 
    //  signInWithEmailAndPassword(auth, username, password);
    if (!remember) {
      
      // signInPromise = auth.setPersistence(inMemoryPersistence).then(
      //   () => signInWithEmailAndPassword(auth, username, password)
      // )
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
