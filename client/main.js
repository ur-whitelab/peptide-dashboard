import Vue from 'vue'
import axios from 'axios'
import App from './components/App'
Vue.http = Vue.prototype.$http = axios
/* eslint-disable no-new */
new Vue({
  components: { App },
  template: '<App/>',
  created: function () {
    this.$mount('#app')
  }
})
