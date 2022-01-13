// not sure what the fuck is going on
// but TFJS is shitting the bed with fetch
import fetch from 'node-fetch';

globalThis.fetch = fetch;
globalThis.Headers = Headers;
globalThis.Request = Request;
globalThis.Response = Response;

import { createApp } from "vue";
import App from './components/App.vue'
const app = createApp(App);
app.mount("#app");
