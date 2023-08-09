import axios from "axios";

axios.defaults.baseURL = import.meta.env.DEV ? "http://localhost:8000/api" : "/api"

class PasteService {
    create = (payload) => axios.post("", payload)
    get = (key) => axios.get(`/${key}`)
    history = (q='') => axios.get(`/history`, {params: {q}})
    delete = (key) => axios.delete(`/${key}`).then(() => {})
    edit = (key, payload) => axios.patch(`/${key}`, payload)
    export = () => axios.get("/export", {responseType: 'blob'})
}

const pasteService = new PasteService();

export default pasteService;
