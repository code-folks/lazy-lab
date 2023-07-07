import { Models } from 'appwrite';
import { defineStore } from 'pinia';
import { Ref, ref, computed, watch } from 'vue';
import { isDefined, useLocalStorage } from '@vueuse/core';

import { useAppWrite } from '../composables';

export type UserPreferences = {
};

export interface AuthSignInResult {
  
};

const USER_REMEMBER_ME_TOKEN = 'user.RememberMe';
const CURRENT_SESSION_TOKEN = 'current';

export const useAuth = defineStore('auth', () => {
  const user: Ref<Models.User<UserPreferences> | null> = ref(null);
  const session: Ref<Models.Session | null> = ref(null);
  const isLoading: Ref<boolean> = ref(false);
  const isAuthenticated = computed(() => !!user);
  const rememberMe = useLocalStorage(USER_REMEMBER_ME_TOKEN, false);
  const { account } = useAppWrite();

  watch(
    session,
    (next, prev) => {
      if(isDefined(next)) {
        isLoading.value = true;
        account.get().then(
          u => {
            user.value = u;
          }
        ).finally(
          () => isLoading.value = false
        );
      } else {
        user.value = null;
      }
    }
  )
  
  if(rememberMe.value) {
    account.getSession(CURRENT_SESSION_TOKEN).then(
      (s: Models.Session) => {
        session.value = s;
      }
    ).finally(
      ()=> isLoading.value = false
    ).catch(
      () => session.value = null
    );
  }

  function signIn(username: string, password: string) {
    isLoading.value = true;
    const signInPromise = account.createEmailSession(username, password);
    signInPromise.finally(
      () => isLoading.value = false
    )
    return signInPromise.then(
      (s: Models.Session) => {
        session.value = s;
        return s;
      }
    )
  }

  return {
    isAuthenticated,
    isLoading,
    rememberMe,
    user,
    session,
    signIn,
    account,
  }
});
