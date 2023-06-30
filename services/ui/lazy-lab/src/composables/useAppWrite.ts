
import { createSharedComposable, toRef } from '@vueuse/core';
import { Ref } from 'vue';
import { Client, Account } from 'appwrite';


interface useAppWriteComposable {
    endpoint: Ref<string>;
    projectId: Ref<string>;
    client: Client;
    account: Account;
}


export function $useAppWrite(): useAppWriteComposable {
    const endpoint: Ref<string> = toRef(import.meta.env.VITE_APPWRITE_ENDPOINT);
    const projectId: Ref<string> = toRef(import.meta.env.VITE_APPWRITE_PROJECT_ID);
    const client = new Client();
    
    client.setEndpoint(endpoint.value);
    client.setProject(projectId.value);

    const account = new Account(client);
    
    return {
        endpoint,
        projectId,
        client,
        account
    }
}

const useAppWrite = createSharedComposable($useAppWrite);


export {
    useAppWrite,
}