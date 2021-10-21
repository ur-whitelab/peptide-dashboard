import Vue from 'vue'
import App from './components/App.vue'
/* eslint-disable no-new */
new Vue({
  components: { App },
  template: '<App/>',
  created: function () {
    this.$mount('#app')
  }
})
