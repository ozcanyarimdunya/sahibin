import Clipboard from "clipboard";
import {ref} from "vue";

const copy2Clipboard = (text) => {
    return new Promise((resolve, reject) => {
        const el = document.createElement('button')
        const clipboard = new Clipboard(el, {
            text: () => text,
            action: () => 'copy',
            container: document.body
        })
        clipboard.on('success', e => {
            clipboard.destroy()
            resolve(e)
        })
        clipboard.on('error', e => {
            clipboard.destroy()
            reject(e)
        })
        el.click()
    })
}

export const useClipboard = () => {
    const copied = ref(false)
    const copy = async (text) => {
        await copy2Clipboard(text)
        copied.value = true
        setTimeout(() => copied.value = false, 1500)
    }
    return {copy, copied}
}


export const useCookie = () => {
    const get = (cookieName, defaultValue = null) => {
        const cookies = document.cookie.split('; ');
        for (const cookie of cookies) {
            const [name, value] = cookie.split("=")
            if (name === cookieName) {
                return decodeURIComponent(value);
            }
        }
        return defaultValue ? decodeURIComponent(defaultValue) : null;
    }
    const set = (cookieName, cookieValue, daysToExpire) => {
        const expirationDate = new Date();
        expirationDate.setDate(expirationDate.getDate() + daysToExpire)
        document.cookie = `${encodeURIComponent(cookieName)}=${encodeURIComponent(cookieValue)};expires=${expirationDate.toUTCString()};path=/`;
    }

    const remove = (cookieName) => {
        document.cookie = `${encodeURIComponent(cookieName)}=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/`;
    }

    return {get, set, remove}
}

export const generateRandomString = (length = 18) => {
    const charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let randomString = "";
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        randomString += charset.charAt(randomIndex);
    }
    return randomString;
}
