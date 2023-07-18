import axios from "axios";

axios.defaults.baseURL = import.meta.env.DEV ? "http://localhost:8000/api" : "/api"

class PasteService {
    create = (payload) => axios.post("", payload).then(({data}) => data)
    get = (key) => axios.get(`/${key}`).then(({data}) => data)
}

const pasteService = new PasteService();

export default pasteService;
