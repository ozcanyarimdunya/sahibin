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
