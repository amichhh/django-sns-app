import axios from "axios";
axios.defaults.baseURL = 'https://localhost:8000/';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// メッセージを検索します
export const findMessages = (param: Object) => {
  axios.get('api/findmessage/', { params: param })
    .then((response) => {
      return response.data
    }).catch((error) => {
      console.log(error)
    }) 
}